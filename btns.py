from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnss = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="/menu")],
    [KeyboardButton(text='/help')],
    [KeyboardButton(text="/<back")],
], resize_keyboard=True)



menu_btns = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="KS"), KeyboardButton(text="KS beginner")],
        [KeyboardButton(text="Foundation")],
        [KeyboardButton(text="Frontend"), KeyboardButton(text="Backend"), KeyboardButton(text="Fullstack")]
    ], resize_keyboard=True
)