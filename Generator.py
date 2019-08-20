
# Generator provides a quick way
# (We don’t need to write __next__ and __iter__ methods here)



###################### Generator Function ########################
print("###################### Generator Function ########################")

# Generator-Function : A generator-function is defined like a normal function,
# but whenever it needs to generate a value, it does so with the yield keyword
# rather than return. If the body of a def contains yield, the function automatically
# becomes a generator function.

def simpleGeneratorFuntion():

    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFuntion():
    print(value)



###################### Generator Object ########################
print("###################### Generator Object ########################")

# Generator-Object : Generator functions return a generator object.
# Generator objects are used either by calling the next method on the generator
# object or using the generator object in a “for in” loop (as shown in the above program).

generator_Object = simpleGeneratorFuntion()


print(next(generator_Object))
# Or
print(generator_Object.__next__())
print(next(generator_Object))