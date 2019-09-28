
import jwt
from bson import ObjectId
import aiohttp.web
from .logger import logger

JWT_ALGORITHM = 'HS256'

async def jwt_middleware(app, handler):
    async def middleware(request: aiohttp.web.Request):
        request.jwt_payload = {}
        jwt_token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, verify=False, algorithms=[JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError) as e:
                # return to_response(*fail('Token is invalid'))
                logger.error(e)
                return await handler(request)
            else:
                request.jwt_payload = payload
        else:
            logger.debug('no Authorization header')
        return await handler(request)
    return middleware
