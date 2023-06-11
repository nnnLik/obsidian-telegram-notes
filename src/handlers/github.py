import logging

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import dp

from src.models.repository import Repository
from src.models.account import Account
from src.services.database import GinoConnection
from src.services.states import RegisterRepositoryState
from src.utils.config import POSTGRES_URL

logger = logging.getLogger(__name__)


async def cmd_connect(message: types.Message):
    user_tg_id = message.from_user.id

    async with GinoConnection(POSTGRES_URL):
        account = await Account.query.where(
            Account.tg_id == user_tg_id
        ).gino.first()

        if not account:
            await message.reply("Please use the /start command first to create an account.")
            return

        await message.reply("Please enter the repository owner:")
        logger.info("Creating a repository connection...")
        await RegisterRepositoryState.owner.set()


@dp.message_handler(state=RegisterRepositoryState.owner)
async def process_owner(message: types.Message, state: FSMContext):
    owner = message.text

    async with state.proxy() as data:
        data['owner'] = owner

    await message.reply("Please enter the repository name:")
    await RegisterRepositoryState.name.set()


@dp.message_handler(state=RegisterRepositoryState.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text

    async with state.proxy() as data:
        data['name'] = name

    await message.reply("Please enter the access token:")
    await RegisterRepositoryState.token.set()


@dp.message_handler(state=RegisterRepositoryState.token)
async def process_token(message: types.Message, state: FSMContext):
    token = message.text

    async with state.proxy() as data:
        data['token'] = token

    async with GinoConnection(POSTGRES_URL):
        async with state.proxy() as data:
            new_repository = Repository(
                user_id=data['account'].id,
                repo_owner=data['owner'],
                repo_name=data['name'],
                access_token=data['token']
            )
            await new_repository.create()

    await state.finish()
    await message.reply("Repository connected successfully!")


dp.register_message_handler(process_owner, state=RegisterRepositoryState.owner)
dp.register_message_handler(process_name, state=RegisterRepositoryState.name)
dp.register_message_handler(process_token, state=RegisterRepositoryState.token)
