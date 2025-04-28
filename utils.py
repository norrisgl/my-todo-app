def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of to-do items."""
    with open(filepath, "r") as data:
        todos_list = data.readlines()

    return todos_list


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the to-do items list in the text file."""
    with open(filepath, "w") as f:
        f.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")
