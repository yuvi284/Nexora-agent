from pydantic import BaseModel
from typing import List

class FileItem(BaseModel):
    path: str
    content: str

class CodingOutput(BaseModel):
    files: List[FileItem]
    run_command: str
    test_command: str