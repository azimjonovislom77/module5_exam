
from db import db_conn
from models import User, Todo
from hash import hash_password, check_password
from colorama import Fore


def green_color(message):
    return Fore.LIGHTGREEN_EX + message + Fore.RESET


def red_color(message):
    return Fore.LIGHTRED_EX + message + Fore.RESET


class UserService:
    @staticmethod
    def register(username, password):
        hashed_password = hash_password(password)
        conn = db_conn()
        cur = conn.cursor()
        try:
            cur.execute(
                'INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id;',
                (username, hashed_password),
            )
            user_id = cur.fetchone()[0]
            conn.commit()
            return User(username, None, user_id)
        except Exception as e:
            print('Error', e)
            return None
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def login(username, password):
        conn = db_conn()
        cur = conn.cursor()
        try:
            cur.execute('SELECT id, username, password, is_admin FROM users WHERE username=%s;', (username,))
            data = cur.fetchone()
            if data and check_password(password, data[2]):
                return User(data[1], None, data[0], is_admin=data[3])
        except Exception as e:
            print('Error', e)
        finally:
            cur.close()
            conn.close()
        return None

    @staticmethod
    def get_all_users():
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, username, is_admin FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users


class TodoService:
    @staticmethod
    def create_todo(user_id, title, description):
        conn = db_conn()
        cur = conn.cursor()
        try:
            cur.execute(
                'INSERT INTO todos (user_id, title, description) VALUES (%s, %s, %s) RETURNING id;',
                (user_id, title, description)
            )
            todo_id = cur.fetchone()[0]
            conn.commit()
            return Todo(todo_id, title, description, user_id)
        except Exception as e:
            print('Error', e)
            return None
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def get_todos(user_id):
        conn = db_conn()
        cur = conn.cursor()
        try:
            cur.execute('SELECT id, title, description FROM todos WHERE user_id=%s;', (user_id,))
            todos = cur.fetchall()
            return [Todo(row[0], row[1], row[2], user_id) for row in todos]
        except Exception as e:
            print('Error', e)
            return []
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def delete_todo(todo_id, user_id):
        conn = db_conn()
        cur = conn.cursor()
        try:
            cur.execute('DELETE FROM todos WHERE id=%s AND user_id=%s RETURNING id;', (todo_id, user_id))
            deleted_todo = cur.fetchone()
            conn.commit()
            return green_color('Todo deleted successfully') if deleted_todo else red_color('Todo not found')
        except Exception as e:
            print('Error', e)
            return red_color('Error deleting todo')
        finally:
            cur.close()
            conn.close()
