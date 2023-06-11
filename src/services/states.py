from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterRepositoryState(StatesGroup):
    owner = State()
    name = State()
    token = State()
