FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    with open(filepath, "r") as file:
        local_todos = file.readlines()
    return local_todos


def write_todos(todos_arg, filepath = FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

