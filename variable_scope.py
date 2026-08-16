'''
LEGB: Local, Enclosing, Global, Built-in
'''

import builtins

print("Total builtins: ", len(dir(builtins)))

def min():
    pass

try:
    m = min([2, 3, 4, 5, 6])
except Exception as e:
    print("Error: ", e)
    print("python goes for global first rather than built-in")
else:
    print(m)


x = 'global x'

def test():
    global y
    y = 'local y'
    # print(y)


print(x)
test()

try:
    print("local --> Global: ", y)
except Exception as e:
    print('Error: ', e)
    print('Error occcured cause y is a local variable')

z = 'global z'

def outer():
    z = 'outer z'

    def inner():
        # global z
        # nonlocal z
        z = 'inner z'
        print(z)

    inner()
    print(z)

outer()
print(z)