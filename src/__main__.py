import os
import aiohttp_cors
import urllib.parse
from aiohttp import web

from motor.motor_asyncio import AsyncIOMotorClient
from tartiflette_aiohttp import register_graphql_handlers
import asyncio

from .middleware import jwt_middleware
from .support import Ctx
import src.scalars
from .engine import CustomEngine
from .constants import DB_URL

here = os.path.dirname(os.path.abspath(__file__))


def build(db):
    app = web.Application(middlewares=[jwt_middleware])
    app.db = db
    context = Ctx(db=db, app=app, loop=None)
    app = register_graphql_handlers(
        app=app,
        engine=CustomEngine(),
        engine_sdl=f"{here}/sdl/",
        executor_context=context,
        executor_http_endpoint="/",
        executor_http_methods=["POST", "GET"],
        graphiql_enabled=True,
    )
    cors = aiohttp_cors.setup(
        app,
        defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True, expose_headers="*", allow_headers="*"
            )
        },
    )
    for route in list(app.router.routes()):
        cors.add(route)

    async def on_startup(app):
        context["loop"] = asyncio.get_event_loop()

    app.on_startup.append(on_startup)
    return app


if __name__ == "__main__":
    db: AsyncIOMotorClient = AsyncIOMotorClient(DB_URL).get_database()
    web.run_app(build(db))

