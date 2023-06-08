import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logger.warning(f"Incoming message: {message.from_user.username}: {message.text}")

    async def on_pre_process_callback_query(
        self, callback_query: types.CallbackQuery, data: dict
    ):
        logger.warning(
            f"Incoming callback query: {callback_query.from_user.username}: {callback_query.data}"
        )

    async def on_post_process_message_handler(self, message: types.Message, data: dict):
        logger.warning(f"Outgoing message: {message.chat.username}: {message.text}")

    async def on_post_process_callback_query_handler(
        self, callback_query: types.CallbackQuery, data: dict
    ):
        logger.warning(
            f"Outgoing callback query: {callback_query.message.chat.username}: {callback_query.data}"
        )
