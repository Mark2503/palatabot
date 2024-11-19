from bot.bot import bot

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception:
        bot.polling(none_stop=True)
