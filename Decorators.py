
# Normal div function
def div(a,b):
    print(a/b)

# Smart div function, where numerator is always greater than denominator
def smart_div(func):

    def inner(a,b):
        if a < b:
            a,b = b,a

        return func(a,b)

    return inner

# Referring normal div to smart div
div = smart_div(div)

# Function calling, smart div is called
div(4,2)
div(2,4)