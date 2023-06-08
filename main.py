import logging

from aiogram import executor
from aiogram import Bot, Dispatcher

from src.handlers.start import cmd_start
from src.utils.config import API_TOKEN
from src.middlewares.logs import LoggingMiddleware

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(cmd_start, commands=["start"])

dp.middleware.setup(LoggingMiddleware())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
