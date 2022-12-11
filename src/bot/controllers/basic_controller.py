from ...bot import telegram_bot, dp, types

@dp.message_handler(commands = ['start'])
async def handle_start(message: types.Message):
    print(message.from_user.id)
    await telegram_bot.send_message(message.from_user.id, "Hi!")