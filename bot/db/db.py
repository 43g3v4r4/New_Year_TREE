import sqlite3
import mysql.connector
from loguru import logger


# Работа с БД
async def connector_db_sqlite(base, query, data):
    # connector_db('base.db', 'SELECT * FROM users WHERE telegram_id = 263604425', '')
    # connector_db('base.db', 'INSERT INTO users (telegram_id, first_name) VALUES (263604425, "Катя")', '')
    # connector_db('base.db', 'UPDATE users SET first_name="Паша" WHERE id=1', '')

    if type(data) == type([]):
        con = sqlite3.connect(base)
        cur = con.cursor()

        cur.executemany(f'{query}', (data))

        result = cur.fetchall()

        con.commit()
        con.close()

    else:
        con = sqlite3.connect(base)
        cur = con.cursor()

        cur.execute(f'{query}')
        result = cur.fetchall()

        con.commit()
        con.close()

    return query, result


# Работа с БД
def connector_db_sqlite_no_async(base, query, data):
    # connector_db('base.db', 'SELECT * FROM users WHERE telegram_id = 263604425', '')
    # connector_db('base.db', 'INSERT INTO users (telegram_id, first_name) VALUES (263604425, "Катя")', '')
    # connector_db('base.db', 'UPDATE users SET first_name="Паша" WHERE id=1', '')

    if type(data) == type([]):
        con = sqlite3.connect(base)
        cur = con.cursor()

        cur.executemany(f'{query}', (data))

        result = cur.fetchall()

        con.commit()
        con.close()

    else:
        con = sqlite3.connect(base)
        cur = con.cursor()

        cur.execute(f'{query}')
        result = cur.fetchall()

        con.commit()
        con.close()

    return query, result


# Работа с БД
def connector_db(dbconfig: dict, query: str, execute: str, **data: list) -> list:
    # connector_db(dbconfig, f'SELECT * FROM users WHERE telegram_id = 263604425', 'execute')
    # connector_db(dbconfig', f'INSERT INTO users (telegram_id, first_name) VALUES (263604425, "Катя")', 'execute')
    # connector_db(dbconfig', f'UPDATE users SET first_name="Паша" WHERE id=1', 'execute')

    # connector_db(dbconfig', f'INSERT INTO products (name) VALUES (%s), 'executemany', data = [[1], [2]]')
    response = []

    try:
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()

        if execute == 'execute':
            cursor.execute(f'{query}')
        elif execute == 'executemany':
            cursor.executemany(f'{query}', data['data'])

        try:
            response = cursor.fetchall()
        except (Exception,):
            pass

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        logger.exception(f'[!] Error: can"t connect to mysql | {e}')

    return response