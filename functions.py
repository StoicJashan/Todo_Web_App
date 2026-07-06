FILEPATH = 'todos_storage.txt'

def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns 
    the list of to-do Items.
    """
    with open(filepath, 'r') as file_local:
      todos_call = file_local.readlines()
    return todos_call

def write_todos(todos_arg,filepath = FILEPATH):
        """ Write the to-do items in a text file."""
        with open(filepath, 'w') as file:
            file.writelines(todos_arg)

if __name__ == "__main__":
     print(get_todos())