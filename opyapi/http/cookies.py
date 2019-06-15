from typing import Optional
from datetime import datetime
from http.cookies import SimpleCookie


class Cookie:
    def __init__(
        self,
        name: str,
        value: str,
        path: Optional[str] = None,
        domain: Optional[str] = None,
        expires: Optional[datetime] = None,
    ):
        pass
