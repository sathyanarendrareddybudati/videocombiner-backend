from pydantic import BaseModel
from typing import Optional

class JobStatus(BaseModel):
    status: str
    download_url: Optional[str] = None
