from fastapi.websockets import WebSocket
import logging

from fastapi.websockets import WebSocketDisconnect

logger = logging.getLogger(__name__)

from main import CommandHandlerFactory


@router.websocket("/ws")  # noqa
async def websocket_handler(
    uow: UOWDep,  # noqa
    websocket: WebSocket,
    user_service: UserServiceDep,  # noqa
    connection_manager: ConnectionManagerDep,
):  # noqa
    await websocket.accept()
    user = None  # можна перетворити в клас або в словник щоб змінювати на цьому рівні
    while True:
        request_data = await websocket.receive_json()
        command = request_data.get("command")
        payload = request_data.get("payload")

        handler_instance = CommandHandlerFactory().get_handler(command)
        QUERY = await handler_instance.handle(payload, websocket, user)
        await websocket.send_json(QUERY)
