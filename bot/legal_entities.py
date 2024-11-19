from bot.bot import bot
from telebot import types
from work_database.workdb import WorkDb
from create_db import DATABASE
from settings import BOT


def parser_text(data: tuple) -> str:
   """
   :param data:
   :return:
   """
   text = f'id: {data[1]}\n' \
          f'Имя: {data[2]}\n' \
          f'Фамилия: {data[3]}\n' \
          f'Организация: {data[4]}\n'\
          f'Паспорт: {data[5]}\n' \
          f'ИНН: {data[6]}\n' \
          f'Телефон: {data[7]}\n' \
          f'Обращение: {data[8]}\n'

   return text


def input_surame_legal_entities(message, *args):
   """
   :param message:
   :param args:
   :return:
   """
   data_options = args[1]
   user_data = args[0]
   user_data[message.from_user.id]['params'].append(message.text)

   text: str = data_options['surname']
   bot.send_message(message.chat.id, text)
   bot.register_next_step_handler(message, input_organization_legal_entities, user_data, data_options)


def input_organization_legal_entities(message, *args):
   """
   :param message:
   :param args:
   :return:
   """
   data_options = args[1]
   user_data = args[0]
   user_data[message.from_user.id]['params'].append(message.text)

   text: str = data_options['organization']
   bot.send_message(message.chat.id, text)
   bot.register_next_step_handler(message, input_passport_legal_entities, user_data, data_options)


def input_passport_legal_entities(message, *args):
   """
   :param message:
   :param args:
   :return:
   """
   data_options = args[1]
   user_data = args[0]
   user_data[message.from_user.id]['params'].append(message.text)

   text: str = data_options['passport']
   bot.send_message(message.chat.id, text)
   bot.register_next_step_handler(message, input_inn_legal_entities, user_data, data_options)


def input_inn_legal_entities(message, *args):
   """
   :param message:
   :param args:
   :return:
   """
   data_options = args[1]
   user_data = args[0]
   user_data[message.from_user.id]['params'].append(message.text)

   text: str = data_options['inn']
   bot.send_message(message.chat.id, text)
   bot.register_next_step_handler(message, input_telephone_legal_entities, user_data, data_options)


def input_telephone_legal_entities(message, *args):
   """
   :param message:
   :param args:
   :return:
   """
   data_options = args[1]
   user_data = args[0]
   user_data[message.from_user.id]['params'].append(message.text)

   text: str = data_options['telefon']
   bot.send_message(message.chat.id, text)
   bot.register_next_step_handler(message, input_messages_legal_entities, user_data, data_options)


def input_messages_legal_entities(message, *args):
   """
   :param message:
   :param args:
   :return:
   """
   data_options = args[1]
   user_data = args[0]
   user_data[message.from_user.id]['params'].append(message.text)

   text: str = data_options['message']
   bot.send_message(message.chat.id, text)
   bot.register_next_step_handler(message, colections_data_legal_entities, user_data, data_options)


def colections_data_legal_entities(message, *args):
    """
    :param message:
    :param args:
    :return:
    """
    user_data = args[0]
    user_data[message.from_user.id]['params'].append(message.text)
    result = [tuple(user_data[message.from_user.id]['params'])]

    wb = WorkDb(DATABASE)
    wb.insert_into_table('legal_entities', result)
    result_data = wb.select_table_bd("SELECT * FROM legal_entities")
    print(result_data)
    text = parser_text(result_data[-1])
    print(text)

    markup = types.InlineKeyboardMarkup()
    btn_url = types.InlineKeyboardButton(text='Ответить', url=BOT['url'])
    markup.add(btn_url)

    bot.send_message(message.chat.id,
                     'Спасибо за обращение\nЕсли хотите отправиь еще одно сообщение нажмите - /start\n')
    bot.send_message(chat_id=BOT['id_channel'], text=text, reply_markup=markup)

