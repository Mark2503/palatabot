from telebot import types

LANGUAGE = {

    'RUS': {
        'choice_options': 'Выберите пожалуйста одни из вариантов!',
        'button': [types.KeyboardButton('Юридическое лицо'), types.KeyboardButton('Физическое лицо')]},
    'Юридическое лицо': {
        'name': "Введите свое имя:",
        'surname': 'Введите свою фамилию:',
        'organization': 'Введите название своей организации:',
        'passport': 'Введите серию своего паспорта:',
        'inn': 'Введите ИНН вашей организации:',
        'telefon': 'Введите ваш телефонный номер:',
        'message': 'Напишите ваще сообщение:'
    },
    'Физическое лицо': {
        'name': "Введите ваше имя:",
        'surname': 'Введите свою фамилию:',
        'passport': 'Введите серию своего паспорта:',
        'telefon': 'Введите ваш телефонный номер:',
        'message': 'Напишите ваще сообщение:'
    },

    'UZB': {
        'choice_options': 'Iltimos, variantlardan birini tanlang!',
        'button': [types.KeyboardButton('Yuridik shaxs'), types.KeyboardButton('Jismoniy shaxs')]},
    'Yuridik shaxs': {
        'name': "Ismingizni kiriting:",
        'surname': 'Familiyangizni kiriting:',
        'organization': 'Tashkilotingiz nomini kiriting:',
        'passport': 'Pasportingiz seriyasini kiriting:',
        'inn': 'Tashkilotingizning tin raqamini kiriting:',
        'telefon': 'Telefon raqamingizni kiriting:',
        'message': 'Xabaringizni yozing:'
    },
    'Jismoniy shaxs': {
        'name': "Ismingizni kiriting:",
        'surname': 'Familiyangizni kiriting:',
        'passport': 'Pasportingiz seriyasini kiriting:',
        'telefon': 'Telefon raqamingizni kiriting:',
        'message': 'Xabaringizni yozing:'
    },
}
