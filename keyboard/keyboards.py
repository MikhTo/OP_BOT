from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup, ReplyKeyboardMarkup)

from lexicon.lexicon import LEXICON_RU


def get_inline_markup(row_width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    inline_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=row_width)
    if args:
        [inline_kb.insert(InlineKeyboardButton(
                            text=LEXICON_RU[button],
                            callback_data=button)) for button in args]
    if kwargs:
        [inline_kb.insert(InlineKeyboardButton(
                            text=text,
                            callback_data=button)) for button, text in kwargs.items()]
                            
    return inline_kb

def get_simple_markup(row_width: int, *args) -> ReplyKeyboardMarkup:
    simple_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(row_width=row_width)
    button_list: list[ReplyKeyboardMarkup] = [ReplyKeyboardMarkup(LEXICON_RU[button]) if button in LEXICON_RU
                                        else ReplyKeyboardMarkup(button) for button in args]
    simple_kb.insert(button_list)               
    return simple_kb

start_menu_kb: ReplyKeyboardMarkup = get_simple_markup(1, *["check_task_sm", "ask_advice", "get_conspectus"])