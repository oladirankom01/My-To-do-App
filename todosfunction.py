def get_todos(filepath=rf'todos.txt'):
    """ Read a text file and return the list of to-do items"""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local 

def write_todos(todos_arg, filepath=rf'todos.txt'):
    """ Write the to-do items list in the text file. """

    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


""" the value that is contained in the variable __name__ is '__main__'
 if ran by the main file (in this instance todosfunction.py)). 
 the value of __name__ is whatever the name of the file that its being held in
if ran from another file (in this instance section15day14.py) """
if __name__ == "__main__": #this module (__name__ == "__main__") makes the lines of code below only execute on todosfunction.py and not section15day14.py.
    print("hello but only in todosfunction")
    print(get_todos())