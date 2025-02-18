from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import menu_start
from loader import dp



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menu_start)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def message_video(message:types.Message):
    fail_id = message.video.file_id
    await message.answer(fail_id)

@dp.callback_query_handler(text="kinolar")
async def message_video(call: types.CallbackQuery):
    url = "https://youtu.be/dJFN7UbwSUk"
    await call.message.answer(url)

@dp.callback_query_handler(text="rasm")
async def message_video(call: types.CallbackQuery):
    url = "https://youtu.be/dJFN7UbwSUk"
    await call.message.answer(url)


