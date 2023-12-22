from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    name = State()
    phone_number = State()
    modme_id = State()
    modme_pass = State()


class AddProductState(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()