import __Name__Sample1


# Here import statement is executed first
# Due to which that file code is executed first
# In both the files we are printing value of __name__
# Value of __name__ :
# if imported file __name__ --> imported_file_name
# if running file  __name__ --> __main__


def add():
    print("Addition function __name__ =", __name__)


def sub():
    print("Subtraction function __name__=", __name__)


def main():
    add()
    sub()
    __Name__Sample1.foo1()
    __Name__Sample1.foo2()


if __name__ == "__main__":
    main()
