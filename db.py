
import psycopg2

db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '7777777',
    'database': 'module5exam',
    'port': 5432
}


def db_conn():
    conn = psycopg2.connect(**db_info)
    return conn


def create_table():
    conn = db_conn()
    if not conn:
        print('Error to conn base')
        return
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_admin BOOLEAN DEFAULT FALSE
        );
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(id) ON DELETE CASCADE,
            title VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    conn.commit()
    cur.close()
    conn.close()

