x = 100

def func():
    global x
    x = 200
    print(x)

func()
print(x)
