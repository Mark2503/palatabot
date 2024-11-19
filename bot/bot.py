import telebot
from telebot import types
from work_database.workdb import WorkDb
from bot.language import LANGUAGE
from settings import BOT
from create_db import DATABASE

bot = telebot.TeleBot(BOT['TOKEN'])

# --------------------- Часть кода которя обработывает запросы граждан ------------------- #


@bot.message_handler(commands=['start'])
def change_language(message):
	"""
	Функция change_language дает пользовтелю возможность выбрать язык, который ему нужен.
	:param message:
	:return:
	"""
	user_data = dict()

	user_data[message.from_user.id] = {}
	user_data[message.from_user.id].update({'params': [message.from_user.id]})

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_language: list = [types.KeyboardButton('UZB'), types.KeyboardButton('RUS')]
	markup.add(*button_language)

	text: str = f'Assalomu alaykum. Tilni tanlang\n Здравствуйте. Выберите язык'
	bot.send_message(message.chat.id, text, reply_markup=markup)
	bot.register_next_step_handler(message, choice_options, user_data)


def choice_options(message, *args):

	"""
	Функция choice_options получет сообщение с названием языка,
	который хочет использовать пользователь полсе этого функция формирует текс и кнопки
	на языке, который выбрал пользователь.
	Функция choice_options предоствляет выбор физического или юридического лица
	:param message:
		Переменная message содержит в словоре данные по пользователе
	:return:
	"""

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	button_face: list = LANGUAGE[str(message.text)]['button']
	markup.add(*button_face)

	text: str = LANGUAGE[str(message.text)]['choice_options']
	bot.send_message(message.chat.id, text, reply_markup=markup)
	bot.register_next_step_handler(message, input_name, args[0])


def input_name(message, *args):
	"""
	:param message:
	:return:
	"""
	data_options = LANGUAGE[message.text]

	if message.text in ['Физическое лицо', 'Jismoniy shaxs']:

		from bot.individuals import input_surame_individuals
		text: str = data_options['name']
		bot.send_message(message.chat.id, text)
		bot.register_next_step_handler(message, input_surame_individuals, args[0], data_options)

	elif message.text in ['Юридическое лицо', 'Yuridik shaxs']:
		from bot.legal_entities import input_surame_legal_entities
		text: str = data_options['name']
		bot.send_message(message.chat.id, text)
		bot.register_next_step_handler(message, input_surame_legal_entities, args[0], data_options)


# --------------------- Часть кода которя обработывает запросы администарторов ------------------- #


def parser_text_admin(data: tuple) -> str:

	text = f'Администратор:\n' \
		   f'Ответил на заявку: {data[1]}\n' \
		   f'Ответ на обращение:\n' \
		   f'{data[2]}'

	return text


@bot.message_handler(commands=['admin'])
def command_admin(message):
	"""
	:param message:
	:return:
	"""

	admin_data = dict()

	admin_data[message.from_user.id] = {}
	admin_data[message.from_user.id].update({'params': []})
	bot.send_message(message.chat.id, f'Напишите id заявки: ')
	bot.register_next_step_handler(message, input_mesage_admin, admin_data)


def input_mesage_admin(message, *args):

	admin_data = args[0]
	admin_data[message.from_user.id]['params'].append(message.text)
	bot.send_message(message.chat.id, f'Напишите ответ на обращение пользователя: ')
	bot.register_next_step_handler(message, collections_data_admin, admin_data)


def collections_data_admin(message, *args):
	"""
	:param message:
	:param args:
	:return:
	"""
	admin_data = args[0]
	admin_data[message.from_user.id]['params'].append(message.text)
	result = [tuple(admin_data[message.from_user.id]['params'])]
	wb = WorkDb(DATABASE)
	wb.insert_into_table('admins', result)
	result_data = wb.select_table_bd("SELECT * FROM admins")
	text = parser_text_admin(result_data[-1])
	bot.send_message(chat_id=result_data[-1][1], text=result_data[-1][2])
	bot.send_message(chat_id=BOT['id_channel'], text=text)
	bot.send_message(message.chat.id, 'Если хотите ответить еще на одно обращение нажмите - /admin\n')


def distribution(indiv, legal, admin):
	"""
	:param indiv:
	:param legal:
	:param admin:
	:return:
	"""
	res_indiv = [n[0] for i in admin for n in indiv if i[0] == n[0]]
	res_legal = [n[0] for i in admin for n in legal if i[0] == n[0]]
	return len(res_indiv), len(res_legal)


@bot.message_handler(commands=['stat'])
def change_language(message):
	wb = WorkDb(DATABASE)
	indiv_stat = wb.select_table_bd("SELECT id_user FROM individuals")
	legal_ent_stat = wb.select_table_bd("SELECT id_user FROM legal_entities")
	admin_stat = wb.select_table_bd("SELECT user_id FROM admins")
	print(f'indiv_stat: {indiv_stat}')
	print(f'legal_ent_stat: {legal_ent_stat}')
	print(f'admin_stat: {admin_stat}')

	result = distribution(indiv_stat, legal_ent_stat, admin_stat)
	print(result)

	text = \
		f'Поступило заявок от юридических лиц: {len(legal_ent_stat)}\n' \
		f'Постпило заявок от физичесеих лиц: {len(indiv_stat)}\n' \
		f'============================================\n' \
		f'Ответили на заявки юридическич лиц: {result[1]}\n' \
		f'Ответили на заявки физических лиц: {result[0]}\n' \
		f'Всего ответили на заявок: {len(admin_stat)}'
	bot.send_message(chat_id=BOT['id_channel'], text=text)


