
from db import db_conn
from colorama import Fore


def green_color(message):
    return Fore.LIGHTGREEN_EX + message + Fore.RESET


class Admin:
    @staticmethod
    def set_admin(user_id):
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('UPDATE users SET is_admin=TRUE WHERE id=%s;', (user_id,))
        conn.commit()
        cur.close()
        conn.close()
        return green_color('Admin set successfully')

    @staticmethod
    def delete_user(user_id):
        conn = db_conn()
        cur = conn.cursor()
        try:
            cur.execute('DELETE FROM users WHERE id = %s;', (user_id,))
            conn.commit()
            return f'User {user_id} deleted successfully'
        except Exception as e:
            return f'Error: {e}'
        finally:
            cur.close()
            conn.close()
