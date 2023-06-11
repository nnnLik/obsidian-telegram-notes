import logging

from aiogram import types

from src.models.account import Account
from src.services.database import GinoConnection
from src.utils.config import POSTGRES_URL
from src.utils.config import MESSAGES

logger = logging.getLogger(__name__)


async def cmd_start(message: types.Message):
    user_tg_id = message.from_user.id

    async with GinoConnection(POSTGRES_URL):
        account = await Account.query.where(
            Account.tg_id == user_tg_id
        ).gino.first()

        if account:
            logger.warning("Account already exists in the database.")
        else:
            new_account = Account(tg_id=user_tg_id)
            await new_account.create()
            logger.warning("Account created.")

    await message.reply(MESSAGES["start"])


async def cmd_help(message: types.Message):
    await message.reply(MESSAGES["help"])
