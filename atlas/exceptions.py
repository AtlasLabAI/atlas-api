from typing import Optional


class AtlasException(Exception):
    """Custom exception for Atlas errors."""

    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code
