CREATE TABLE IF NOT EXISTS legal_entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER  NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    organization TEXT NOT NULL,
    passport TEXT NOT NULL,
    inn TEXT NOT NULL,
    telephone TEXT NOT NULL,
    messages TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS individuals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER  NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    passport TEXT NOT NULL,
    telephone TEXT NOT NULL,
    messages TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL
);