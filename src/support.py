import asyncio
from dataclasses import dataclass
from aiohttp.web import Application
from motor.core import Database
from dotdict import dotdict


class Ctx(dotdict):
    db: Database
    app: Application
    loop: asyncio.BaseEventLoop