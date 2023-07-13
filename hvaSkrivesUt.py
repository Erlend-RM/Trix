#1)
# 2 skrives ut
a = 2

def endreA():
    a = 5

endreA()
print(a)


#2)
# 2 skrives ut
a = 2

def endreA():
    a = 5

b = endreA()
print(a)


#3)
#5 skrives ut
a = 2

def endreA():
    return 5

a = endreA()
print(a)


#4)
#2 skrives ut
a = 2

def endreA(b):
    b = 5
    return b

endreA(a)
print(a)


#5)
#5 skrives ut
a = 2

def endreA(b):
    b = 5
    return b

a = endreA(a)
print(a)

#6)
#b is not defined
a = 2

def endreA(b):
    b = 5
    return b

a = endreA(a)
print(b)
