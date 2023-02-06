from aiogram import Dispatcher

from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON_RU

from keyboard.keyboards import get_inline_markup, get_simple_markup

ADMIN_ID=829365853


from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from services.file_handling import *


async def process_admin_start_command(message: Message):
    await message.answer(text=f" Приветствую вас, админ! \n Что хотите сделать?",
                        reply_markup=get_inline_markup(1, "add_seminar", "add_marks", "notify_group"))
    
async def process_add_seminar_press(callback: CallbackQuery):
    await callback.message.edit_text("Добавить новый или редактировать старый?",
                                    reply_markup=get_inline_markup(1, "new_sem", "edit_sem"))

async def process_accept_student_press(callback: CallbackQuery):
    student_id=int(callback.message.text.split(" ")[-1]) #мб "data"?
    #add to data base
    await callback.message.bot.send_message(text=LEXICON_RU["greetings"],
                                            chat_id=student_id,
                                            parse_mode="HTML")

async def process_materials_press(message: Message):
    list_of_sems: list[str] = get_seminars_list(LEXICON_RU["materials_directory"])
    await message.answer(text=LEXICON_RU["choose_seminars"], reply_markup=get_inline_markup(1, *list_of_sems, "all_sem"))

async def process_sem_press(callback: CallbackQuery):
    file_bytes = get_materials(callback.data, LEXICON_RU["materials_directory"])
    await callback.message.delete()
    await callback.message.answer_document(document=file_bytes,caption="⬆️"+LEXICON_RU[callback.data],)

async def process_start_new_command(message: Message):
    await message.answer(text=f"ваша заявка отправлена! \n Ожидайте подтверждения от преподавателя")
    await message.bot.send_message(text=f"Заявка от: {message.from_user.full_name}, id: {message.from_user.id}", chat_id=ADMIN_ID,
                            reply_markup=get_inline_markup(2, accept=f"accept: {message.from_user.id}", 
                                                           deny=f"deny: {message.from_user.id}", 
                                                           accept_guest=f"accept_guest: {message.from_user.id}"))

async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["greetings"], parse_mode="HTML")

async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["help"])

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"])
    dp.register_message_handler(process_help_command, commands=["help"])
    dp.register_message_handler(process_materials_press, commands=["materials"])

    dp.register_callback_query_handler(process_sem_press, lambda data: "sem" in data.data)