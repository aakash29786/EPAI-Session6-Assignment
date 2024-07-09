def check_docstring(fn , *args):
    ''' 
    This is a closure function that checks if the function that is being
    passed has at least 50 characters in its docstring
    '''
    char = 50
    if isinstance (fn, int) or isinstance (fn, complex) or isinstance (fn, str):
        raise ValueError ("*Only functions are allowed*")
    elif args:
        raise ValueError ("*Function needs only 1 argument but 2 arguments are passed*")   
    else:         
        def outer():
            val = fn.__doc__
            word_length = len(val.split())
            if word_length > char:
                return 1
            else:
                return 0   
        return outer   

def fibonacci(num):
    ''' 
    This is a closure function that takes a number and gets the fibonacci of that number
    '''
    if isinstance (num, complex) or isinstance (num, str):
        raise ValueError ("*Only postive integers are allowed*")
    elif num < 0:
        raise ValueError ("*Only postive integers are allowed*")
    else:
        fib1 = 1
        fib2 = 1
        def inner():
            for i in range(3 , num+1):
                nonlocal fib1
                nonlocal fib2
                fib1, fib2 = fib2, fib1 + fib2
            return fib2
        return inner

def counter(fn):
    '''
    Decorator function that maintains and updates a global dictionary variable 
    depending on the number of times a function (add /div/ mul) is called.
    '''
    global func_counter_dict
    func_counter_dict = {}
    add_count = 0
    mul_count = 0
    div_count = 0
    def inner(*args, **kwargs):
        nonlocal add_count
        nonlocal mul_count
        nonlocal div_count
        if isinstance (args[0], complex) or isinstance (args[0], str) or args[0] < 0 or args[1]< 0 :
            raise ValueError ("*Only postive integers are allowed*")  
        elif fn.__name__ == "add":            
            add_count += 1
            func_counter_dict["add"] = add_count
            return func_counter_dict
        elif fn.__name__ == "mul":
            mul_count += 1
            func_counter_dict["mul"] = mul_count
            return func_counter_dict
        elif fn.__name__ == "div":
            div_count += 1
            func_counter_dict["div"] = div_count
            return func_counter_dict
    return inner

@counter
def add(x, y):
    return x + y

@counter
def mul(x, y):
    return x * y

@counter
def div(x, y):
    return x / y 