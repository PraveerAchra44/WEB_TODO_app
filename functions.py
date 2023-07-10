def get_todos(filepath='todos.txt'):
    """READ A TEXT FILE AND RETURN THE LIST OF ToDo ITEMS"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath='todos.txt'):
    """WRITE THE TO-DO ITEMS LIST IN THE TEXT FILE."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
