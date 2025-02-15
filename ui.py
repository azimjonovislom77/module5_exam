from services import UserService, TodoService
from admin import Admin
from colorama import Fore

users = UserService()
todos = TodoService()


def red_color(message):
    return Fore.LIGHTRED_EX + message + Fore.RESET


def green_color(message):
    return Fore.LIGHTGREEN_EX + message + Fore.RESET


def menu_color(message):
    return Fore.LIGHTCYAN_EX + message + Fore.RESET


def yellow_color(message):
    return Fore.LIGHTYELLOW_EX + message + Fore.RESET


def todo_menu(user):
    while True:
        print(menu_color('Create todo      --->  1'))
        print(menu_color('Show all todos   --->  2'))
        print(menu_color('Delete todo      --->  3'))
        print(menu_color('Logout           --->  4'))

        choice = input(yellow_color('Choice: '))

        if choice == '1':
            title = input(yellow_color('Title: '))
            description = input(yellow_color('Description: '))
            todos.create_todo(user.id, title, description)
            print(green_color('Todo created successfully'))

        elif choice == '2':
            user_todos = todos.get_todos(user.id)
            if not user_todos:
                print(red_color('No todos found'))
            else:
                print(green_color('All todos: '))
                for todo in user_todos:
                    print(f'{todo.id} - {todo.title} - {todo.description}')

        elif choice == '3':
            todo_id = input(yellow_color('Enter todo_id to delete: '))
            if todo_id.isdigit():
                result = todos.delete_todo(int(todo_id), user.id)
                print(result)
            else:
                print(red_color('ID must be a number'))

        elif choice == '4':
            print(red_color('You are logged out'))
            break


def run():
    current_user = None
    while True:
        print(menu_color('Register       --->   1'))
        print(menu_color('Login          --->   2'))
        print(menu_color('Set_admin      --->   3'))
        print(menu_color('Delete_user    --->   4'))
        print(menu_color('Show all users --->   5'))
        print(menu_color('Exit           --->   6'))

        choice = input(yellow_color('Choice: '))

        if choice == '1':
            username = input(yellow_color('Username: '))
            password = input(yellow_color('Password: '))
            users.register(username, password)
            print(green_color('User registered successfully'))

        elif choice == '2':
            username = input(yellow_color('Username: '))
            password = input(yellow_color('Password: '))
            user = users.login(username, password)
            if user:
                print(green_color('Successfully logged in'))
                current_user = user
                todo_menu(user)
            else:
                print(red_color('Invalid username or password'))

        elif choice == '3':
            all_users = users.get_all_users()
            if not all_users:
                print(red_color('No users found!'))
                continue
            print(green_color('All users: '))
            for u in all_users:
                print(f'{u[0]} - {u[1]} {"(Admin)" if u[2] else ""}')
            admin_id = input(yellow_color('Enter ID to set as admin: '))
            if admin_id.isdigit():
                result = Admin.set_admin(int(admin_id))
                print(result)
            else:
                print(red_color('Admin ID must be a number'))

        elif choice == '4':
            if not current_user or not current_user.is_admin:
                print(red_color('Only admin can delete users'))
                continue

            all_users = users.get_all_users()
            if not all_users:
                print(red_color('No users found'))
                continue
            print(green_color('All users:'))
            for u in all_users:
                print(f'{u[0]} - {u[1]} {"(Admin)" if u[2] else ""}')
            user_id = input(yellow_color('Enter user_id to delete: '))
            if user_id.isdigit():
                result = Admin.delete_user(int(user_id))
                print(result)
            else:
                print(red_color('ID must be a number'))

        elif choice == '5':
            all_users = users.get_all_users()
            if not all_users:
                print(red_color('No users found'))
                continue
            print(green_color('All users:'))
            for u in all_users:
                print(f'{u[0]} - {u[1]} {"(Admin)" if u[2] else ""}')

        elif choice == '6':
            print(red_color('Goodbye!'))
            break


if __name__ == '__main__':
    run()
