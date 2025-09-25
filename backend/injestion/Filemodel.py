from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FileMetadata(BaseModel):
    id: Optional[str] = None
    filename: str
    content_type: str
    s3_path: str
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)

