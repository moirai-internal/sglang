import logging

from fastapi import Request
from starlette.types import Receive, Scope, Send

logger = logging.getLogger("fastapi")


class OpcRequestIdMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or scope["method"] != "POST":
            await self.app(scope, receive, send)
            return

        request = Request(scope, receive=receive)
        opc_request_id = request.headers.get("opc-request-id", None)
        logger.info(
            "FastAPI Server: Receive request opc-request-id: %s", opc_request_id
        )

        try:

            async def custom_receive():
                message = await receive()
                if message["type"] == "http.disconnect":
                    logger.info(
                        "Client disconnected for request opc-request-id: %s",
                        opc_request_id,
                    )
                return message

            async def custom_send(message):
                if message["type"] == "http.response.start":
                    status_code = message["status"]
                    logger.info(
                        "FastAPI Server: Start response for request opc-request-id: %s, status_code: %s",
                        opc_request_id,
                        status_code,
                    )
                elif message["type"] == "http.response.body" and not message.get(
                    "more_body", False
                ):
                    logger.info(
                        "FastAPI Server: Finish response for request opc-request-id: %s",
                        opc_request_id,
                    )

                await send(message)

            await self.app(scope, custom_receive, custom_send)

        except Exception as e:
            logger.error(
                "Exception during opc-request-id: %s, error: %s",
                opc_request_id,
                str(e),
            )
            raise
