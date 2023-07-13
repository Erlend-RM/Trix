#global variabel
a = 9
#global variabel
b = 5

def foo(a):
    if a > 5:
        bar()
    else:
        baz(a)

def bar():
    if a >= 8:
        print(a)
    else:
        print("***")
    return 5

def baz(b):
    #lokal variabel
    c = b + bar()
    print(c)

a = 8

#kommer til å skrive ut: printer 8
foo(7)
#kommer til å skrive ut: printer 8 på en linje også 9 på neste
foo(4)
