from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

cng_acc_btn = KeyboardButton("📝 Изменить аккаунт")
unreads_btn = KeyboardButton("📒 Вывести недочитанные")
bookmarks_btn = KeyboardButton("🔖 Вывести закладки")
settings_btn = KeyboardButton("⚙️ Настройки")
menu_btn = KeyboardButton("📋 Меню")
subscribe_btn = '🔊 Подписаться на обновления'
unsubscribe_btn = '🔇 Отписаться от обновлений'


def create_reply_keyboard_markup():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        row_width=1
    )


main_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1
).add(bookmarks_btn, settings_btn)

cng_acc_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1
).add(cng_acc_btn, menu_btn)

settings_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1
).add(cng_acc_btn, menu_btn)
