from aiogram.fsm.state import StatesGroup, State

class RegisterState(StatesGroup):
    regName = State()
    regcity = State()