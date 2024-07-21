from fastapi import APIRouter, HTTPException, File, UploadFile
from typing import List
from uuid import uuid4
import logging
from celery.result import AsyncResult
from celery_app import app
from routes.tasks import combine_videos

router = APIRouter(tags=['Video Combiner'])

job_status = {}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    logger.info("Received file upload request with %d files", len(files))
    
    if len(files) < 1:
        logger.error("Invalid number of files uploaded: %d", len(files))
        raise HTTPException(status_code=400, detail="You must upload more than one files")
    
    job_id = str(uuid4())
    file_paths = []

    try:
        for file in files:
            file_path = f"/tmp/{file.filename}"
            file_paths.append(file_path)
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())
            logger.info("Saved file %s to %s", file.filename, file_path)

        combine_videos.delay(job_id, file_paths)
        
        job_status[job_id] = "Processing"
        logger.info("Dispatched video combining task with job_id: %s", job_id)
        
        return {"job_id": job_id}

    except Exception as e:
        logger.exception("File upload failed")
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")
    


@router.get("/jobs/{job_id}")
async def get_job_status(job_id: str):
    logger.info("Checking status for job_id: %s", job_id)
    task_result = AsyncResult(job_id, app=app)
    if task_result.state == 'SUCCESS':
        download_url = f"/downloads/{job_id}.mp4"
        logger.info("Job %s completed successfully", job_id)
        return {"status": task_result.state, "download_url": download_url}
    elif task_result.state == 'FAILURE':
        logger.error("Job %s failed", job_id)
        raise HTTPException(status_code=500, detail="Job failed.")
    logger.info("Job %s is still processing", job_id)
    return {"status": task_result.state, "detail": "Job is still processing."}
