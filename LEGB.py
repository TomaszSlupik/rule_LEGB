# LEGB - 1 - wynik 10 - zakres globalny
x = 10

def func1 ():
    print(x)

def func2():
    x = 5
    print(func1())


func2()

print ("----")

# przykład 2: wynik => Samsung, Iphone
phoneOne = 'Iphone'

def phoneFirst():
    phoneOne = 'Samsung'
    print(phoneOne)

def phoneSecond():
    phoneFirst()
    print(phoneOne)

phoneSecond()

print ("----")