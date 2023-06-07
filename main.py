import logging

from decouple import config

from aiogram import executor
from aiogram import Bot, Dispatcher, types

from src.models.base import Account
from src.services.database import GinoConnection

API_TOKEN = "5937195123:AAEklPALiCkhQk6Z9jGQO1xOifxklVutgVU"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    user_tg_id = message.from_user.id
    
    async with GinoConnection(config("POSTGRES_URL")) as db:
        account = await Account.query.where(Account.tg_id == user_tg_id).gino.first()
        print(1)
        if account:
            print(2)
            logger.warning("Account already exists in the database.")
        else:
            print(3)
            new_account = Account(tg_id=user_tg_id)
            await new_account.create()
            logger.warning("Account created.")

    await message.reply("Hello")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
