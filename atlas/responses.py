from typing import Any, Dict


class AtlasResponse:
    """Encapsulates API responses."""

    def __init__(self, data: Dict[str, Any], status_code: int):
        self.data = data
        self.status_code = status_code

    def __repr__(self):
        return f"AtlasResponse(status_code={self.status_code}, data={self.data})"

    def is_successful(self) -> bool:
        return 200 <= self.status_code < 300
