from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FileMetadata(BaseModel):
    id: Optional[str] = Field(alias="_id")
    filename: str
    content_type: str
    s3_path: str
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
