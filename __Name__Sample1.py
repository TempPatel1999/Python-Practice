import __Name__Sample2

# Here import statement is executed first
# Due to which that file code is executed first
# In both the files we are printing value of __name__
# Value of __name__ :
# if imported file __name__ --> imported_file_name
# if running file  __name__ --> __main__


def foo1():
    print("In foo1 __name__ =",__name__)


def foo2():
    print("In foo2 __name__ =",__name__)


def main():
    foo1()
    foo2()
    __Name__Sample2.add()
    __Name__Sample2.sub()


if __name__ == "__main__":
    main()
