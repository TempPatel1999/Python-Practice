# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
#
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().


# Sample working of iterator
list1 = [6,1,6,3]

it = iter(list1)

print(next(it))
print(next(it))


# Customised iterator Class
print("TopTen Class....")

class TopTen:

    def __init__(self):
        self.value = 1

    def __iter__(self):         # Important method of Iterator
        return self

    def __next__(self):         # Important method of Iterator

        if self.value <= 10:
            temp = self.value
            self.value += 1

            return temp

        else:
            raise StopIteration


t1 = TopTen()

for i in t1:
    print(i)