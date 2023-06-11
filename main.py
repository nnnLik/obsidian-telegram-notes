from bot import dp
from src.handlers import cmd_start, cmd_help, cmd_connect
import logging
from aiogram import executor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Started")

    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(cmd_connect, commands=["connect"])

    executor.start_polling(dp, skip_updates=True)
