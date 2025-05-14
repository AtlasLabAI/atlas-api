from typing import Any, Dict

import aiohttp

from .exceptions import AtlasException
from .responses import AtlasResponse


class AtlasAsync:
    """Asynchronous Atlas API Wrapper."""

    BASE_URL = "https://api.atlaslab.io"  # Example base URL, replace with actual

    def __init__(self, grok_api_key: str):
        if not grok_api_key:
            raise AtlasException("API key is required to initialize Atlas")

        self.api_key = grok_api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def post(
        self, endpoint: str, payload: Dict[str, Any], stream: bool = False
    ) -> AtlasResponse:
        url = f"{self.BASE_URL}/{endpoint}"
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                async with session.post(url, json=payload) as response:
                    data = await response.json()
                    if response.status < 200 or response.status >= 300:
                        raise AtlasException(
                            f"Request to Atlas API failed: {response.reason}",
                            status_code=response.status,
                        )
                    return AtlasResponse(data=data, status_code=response.status)
            except Exception as e:
                raise AtlasException(f"Request to Atlas API failed: {e}")

    async def analyze_text(
        self,
        text: str,
        CustomRPC: str = None,
        web_access: bool = False,
        max_token: int = 512,
        temperature: float = 0.7,
        stream: bool = False,
    ) -> AtlasResponse:
        if not text:
            raise AtlasException("The 'text' parameter cannot be empty")

        payload = {
            "text": text,
            "CustomRPC": CustomRPC,
            "web_access": web_access,
            "max_token": max_token,
            "temperature": temperature,
            "stream": stream,
        }

        return await self.post(endpoint="analyze", payload=payload, stream=stream)
