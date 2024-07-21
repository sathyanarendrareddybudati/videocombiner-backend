from celery_app import app
import logging
import os
import subprocess
from typing import List

logger = logging.getLogger(__name__)

@app.task(name='tasks.combine_videos', bind=True)
def combine_videos(self, job_id: str, file_paths: List[str]):
    try:
        # Configurable paths
        temp_dir = os.getenv('TEMP_DIR', '/tmp')
        output_path = os.path.join(temp_dir, f"{job_id}.mp4")
        filelist_path = os.path.join(temp_dir, 'filelist.txt')
        
        logger.info(f"Starting to combine videos for job {job_id}")

        # Ensure the directory for the output file exists
        os.makedirs(temp_dir, exist_ok=True)
        logger.info(f"Using temporary directory {temp_dir}")

        # Check if files exist and log their paths
        for path in file_paths:
            if not os.path.exists(path):
                logger.error(f"File not found: {path}")
                raise FileNotFoundError(f"File not found: {path}")

        # Create filelist.txt
        with open(filelist_path, 'w') as f:
            for path in file_paths:
                f.write(f"file '{path}'\n")
        
        logger.info(f"File list written to {filelist_path}")
        
        with open(filelist_path, 'r') as f:
            logger.info(f"Contents of {filelist_path}:\n{f.read()}")
        
        command = [
            "ffmpeg",
            "-f", "concat",
            "-safe", "0",
            "-i", filelist_path,
            "-c", "copy",
            "-analyzeduration", "5000000",
            "-probesize", "5000000",
            output_path
        ]

        # Run ffmpeg command
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            logger.error(f"ffmpeg error: {result.stderr}")
            self.update_state(state='FAILURE', meta={'exc_type': 'SubprocessError', 'exc_message': result.stderr})
            raise subprocess.CalledProcessError(result.returncode, command, output=result.stdout, stderr=result.stderr)
        
        logger.info(f"Videos combined successfully into {output_path}")
    except FileNotFoundError as fnf_error:
        logger.error(f"File not found error: {str(fnf_error)}", exc_info=True)
        self.update_state(state='FAILURE', meta={'exc_type': type(fnf_error).__name__, 'exc_message': str(fnf_error)})
        raise fnf_error
    except subprocess.CalledProcessError as subproc_error:
        logger.error(f"Subprocess error: {str(subproc_error)}", exc_info=True)
        self.update_state(state='FAILURE', meta={'exc_type': type(subproc_error).__name__, 'exc_message': str(subproc_error)})
        raise subproc_error
    except Exception as e:
        logger.error(f"Failed to combine videos: {str(e)}", exc_info=True)
        self.update_state(state='FAILURE', meta={'exc_type': type(e).__name__, 'exc_message': str(e)})
        raise e
    finally:
        if os.path.exists(filelist_path):
            os.remove(filelist_path)
            logger.info(f"Cleaned up temporary file {filelist_path}")
