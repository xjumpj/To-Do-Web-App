
def get_todos(filepath='todos.txt'):
    """This function reads the file todos.txt.
       The program then saves the contents to variable named todos.  """
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath='todos.txt'):
    """Writes todos into a file named todos.txt"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#This code here is essentially used if we want to test something.
#In this case, we are trying to see the output of the function get_todos().
#Now when we run functions.py, __name__ is set to main, because it is the main file we want to run.
#However, if we were trying to import the functions to another file, __name__ would be equal to 'functions' as that is the file name.
#So if you run a python file, that file would currently be the main file. But since we are importing it to another file, that other file is the main and the name would be functions in this case.
#
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
    