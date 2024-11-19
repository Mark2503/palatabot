from settings import DATABASE
from work_database.workdb import WorkDb


if __name__ == '__main__':
    db = WorkDb(DATABASE)
    db.create_db()
    print('База данных создана')
    db.read_script_sql('table_create.sql')
    print('Таблицы созданы')
