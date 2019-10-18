# Main file
# currently being used for testing purposes
#
# PDP group 25

from testclass import aux

def say_hello():
	print("Hello World")
	print("It Worked!")

if __name__ == '__main__':
	say_hello()
        aux1 = aux(1,2,3)
        aux1.modify_all()
        aux1.print_all()


