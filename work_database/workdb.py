import sqlite3 as sq


class WorkDb:

    def __init__(self, db: dict[str, str]):
        """
        :param db:
        """
        self.__conn = sq.connect(db['database'])
        self.__cur = self.__conn.cursor()

    def create_db(self):
        """
        Метод create_db создает базу данных
        :return:
        """
        try:
            self.__cur.execute("""""")
        except Exception as e:

            return f'Ошибка создания:\n {e}'

    def drop_table_db(self, name_table: str):
        """
        Метод  drop_db удалеет таблицу из базы данных
        :param name_table:
            Атрибут принимает название таблици из базы данных
        :return:
        """
        try:
            self.__cur.execute(f"DROP TABLE {name_table}")
            self.__conn.commit()
        except Exception as e:
            return f'Ошибка:\n {e}'

    def read_script_sql(self, name_file: str):
        """
        Метод read_script_sql работает с файлами sql -> используются  для написания скриптов виде запроса к БД.
        :param name_file:
            Атрибут принимает название файла скрипта для создания таблиц name_file.sql
        :return:
        """
        try:

            with open(name_file, 'r') as file:
                self.__cur.executescript(file.read())
            self.__conn.commit()

        except Exception as e:
            return f'Ошибка создания:\n {e}'

    def __executemany_db(self, params: str):
        """
        Метод __executemany_db является вспомогательным методом для insert_into_table
        :param params:
        :return:
        """
        try:
            self.__cur.executemany(*params)
            self.__conn.commit()

        except Exception as e:
            return f'Ошибка создания:\n {e}'

    def insert_into_table(self, name_table: str, params: list[tuple[str]]):
        """
        Метод insert_into_table добавляет данные в таблицы базы данных
        :param name_table:
            Атрибут name_table принимате название базы данных
        :param params:
            Атрибут params принимате данные которые нужно записать в таблицу базы данных
            Например: parms = [('name', 'surname') ('name', 'surname')]
        :return:
        """
        try:
            if name_table == 'legal_entities':

                self.__executemany_db((f"INSERT INTO {name_table} VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", params))

            elif name_table == 'individuals':

                self.__executemany_db((f"INSERT INTO {name_table} VALUES (NULL, ?, ?, ?, ?, ?, ?)", params))

            elif name_table == 'admins':

                self.__executemany_db((f"INSERT INTO {name_table} VALUES (NULL, ?, ?)", params))

        except Exception as e:
            return f'Ошибка:\n {e}'

    def select_table_bd(self, sql_request: str):
        """
        Метод select_table_bd осуществляет чтение данных из базы даннх
        :param sql_request:
            Атрибут sql_request принимает sql запрос пример: 'SELECT * FROM admins'
            ссылка на уроки по sqllite: https://proproprogs.ru/modules/chto-takoe-subd-i-relyacionnye-bd
        :return:
        """
        try:
            return self.__cur.execute(sql_request).fetchall()

        except Exception as e:
            return f'Ошибка:\n {e}'

    def __del__(self):
        """
        Метод __del__ закрывает базу данных
        :return:
        """
        self.__conn.close()
