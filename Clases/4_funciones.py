d0 = 3
d1 = 6

def suma(a,b):
    s = a + b
    return s

def multi(a,b):
    s = a * b
    return s

def multi_global():
    s = d0 * d1
    return s

if __name__ == "__main__":
    a = 5
    b = 6
    c0 = suma(a,b)
    c1 = multi_global()
    print(c0,c1)
