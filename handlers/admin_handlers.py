from aiogram import Dispatcher

from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON_RU

from keyboard.keyboards import get_inline_markup, get_simple_markup

ADMIN_ID=829365853


async def process_start_command(message: Message):
    await message.answer(text=f" Приветствую вас, админ! \n Что хотите сделать?",
                        reply_markup=get_inline_markup(1, "add_seminar", "add_marks", "notify_group"))
    
async def process_add_seminar_press(callback: CallbackQuery):
    await callback.message.edit_text("Добавить новый или редактировать старый?",
                                    reply_markup=get_inline_markup(1, "new_sem", "edit_sem"))

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=["start"])