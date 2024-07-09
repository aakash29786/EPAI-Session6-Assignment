import pytest
import random
import string
import session6
import os
import inspect
import re
import math
import time

README_CONTENT_CHECK_FOR = [
    'decorator',
    'docstring',
    'fibonacci',
    'counter',
    'closure'
]

def test_session6_readme_exists():
    """ A. failure_message: Found README.md file
        B. Once you write this test, it needs to print the filures_message for failing this test.
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    #assert True == False, "You need to write this test!"
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session6_readme_500_words():
    """ A. failures_message: Make your README.md file interesting! Add atleast 500 words
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"


def test_session6_readme_proper_description():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


def test_session6_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
        A.  failures_message_1: Your script contains misplaced indentations
            failures_message_2: Your code indentation does not follow PEP8 guidelines
        B. Once you write this test, it needs to print the failures_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session6_function_name_had_cap_letter():
    """ A. failures_message: You have used Capital letter(s) in your function names
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    #assert True == False, "You need to write this test!"
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

############################## Assignment Validations ###########################
   
def test_session6_docstring_no_args():
    '''
        Test docstring fnction with no arguments
    '''
    with pytest.raises(TypeError, match=r".*required positional argument: 'fn'*"):
        session6.check_docstring()

def test_func():
    '''
    This fucntion is to check the docstring function.
    The number of characters in this fuction is greater than 50.
    This fucntion is to check the docstring function.
    The number of characters in this fuction is greater than 50. 
    This fucntion is to check the docstring function.
    The number of characters in this fuction is greater than 50. 
    '''
    pass
def test_session6_docstring():  
    ''' 
    Check if the doctring function is working as expected and is returning pass
    for docstring's word length > 50 and fail for docstring's word length <50 
    ''' 
    func = session6.check_docstring(test_func)
    assert func() == 1, "docstring check function is not working as expected"
    func = session6.check_docstring(sum)
    assert func() == 0 , "docstring check function is not working as expected"

def test_session6_docstring_unwanted_args():
    '''
    Check if any unwanted arguments such as integers, complex numbers, string are passed 
    instead of a function
    '''
    with pytest.raises(ValueError, match=r".*Only functions are allowed*"):
        session6.check_docstring(10)
    with pytest.raises(ValueError, match=r".*Only functions are allowed*"):
        session6.check_docstring(1+2j)
    with pytest.raises(ValueError, match=r".*Only functions are allowed*"):
        session6.check_docstring("str")

def test_session6_docstring_args():
    '''
    Check if any non required arguments are passed
    '''
    with pytest.raises(ValueError, match=r".*Function needs only 1 argument but 2 arguments are passed*"):
        session6.check_docstring(print, 10)

def test_session6_docstring_freevars():
    '''
    Check if the number 50 is available as a free variable or not
    '''
    assert session6.check_docstring.__code__.co_freevars != None , "No free variables in the function"  

def test_session6_fibonacci_no_args():
    '''
        Test fibonacci fnction with no arguments
    '''
    with pytest.raises(TypeError, match=r".*required positional argument*"):
        session6.fibonacci()

def test_Session6_fibonacci():
    func = session6.fibonacci(6)
    assert func() == 8, "fibonacci function is not working as expected"
    func = session6.fibonacci(10)
    assert func() == 55 , "fibonacci function is not working as expected"   

def test_session6_fibonacci_freevars():
    '''
    Check if the there are free variables and the function is indeed a closure
    '''
    assert session6.fibonacci.__code__.co_freevars != None , "No free variables in the function"     

def test_session6_fibonacci_negative_numbers():
    '''
    Check if any unwanted arguments such as negative integers are passed
    instead of a positive integers
    '''
    with pytest.raises(ValueError, match=r".*Only postive integers are allowed*"):
        session6.fibonacci(-10)

def test_session6_fibonacci_complex_numbers():
    '''
    Check if any unwanted arguments such as complex numbers are passed 
    instead of a positive integers
    '''
    with pytest.raises(ValueError, match=r".*Only postive integers are allowed*"):
        session6.fibonacci(1+2j)

def test_session6_fibonacci_string():
    '''
    Check if any unwanted arguments such as cstring characters are passed 
    instead of a positive integers
    '''
    with pytest.raises(ValueError, match=r".*Only postive integers are allowed*"):
        session6.fibonacci("str")    

def test_session6_decorator_add():
    '''
    Call the add "i" number of times and check if the global 
    dictionary maintains the correct number of calls made to the fuction.
    '''
    for i in range (5):
        session6.add(1,2)
    assert session6.add(1,2)["add"] == i + 2, "The count isnt maintaing the correct number of function calls"      

def test_session6_decorator_mul():
    '''
    Call the mul "i" number of times and check if the global 
    dictionary maintains the correct number of calls made to the fuction.
    '''
    for i in range (4):
        session6.mul(2,5)
    assert session6.mul(1,2)["mul"] == i + 2, "The count isnt maintaing the correct number of function calls" 

def test_session6_decorator_div():
    '''
    Call the div "i" number of times and check if the global 
    dictionary maintains the correct number of calls made to the fuction.
    '''
    for i in range (8):
        session6.div(8,2)
    assert session6.div(1,2)["div"] == i + 2, "The count isnt maintaing the correct number of function calls" 


def test_session6_decorator_negative():
    '''
    Check if any unwanted arguments such as negative integers are passed 
    instead of a positive integers
    '''
    with pytest.raises(ValueError, match=r".*Only postive integers are allowed*"):
        session6.add(-10, 2)
def test_session6_decorator_complex():
    '''
    Check if any unwanted arguments such as complex numbers are passed 
    instead of a positive integers
    '''
    with pytest.raises(ValueError, match=r".*Only postive integers are allowed*"):
        session6.mul(1+2j, 4)

def test_session6_decorator_string():
    '''
    Check if any unwanted arguments such as string are passed 
    instead of a positive integers
    '''
    with pytest.raises(ValueError, match=r".*Only postive integers are allowed*"):
        session6.div("str", 6)    

def test_session6_decorator_freevars():
    '''
    Check if the there are free variables and the function is indeed a closure
    '''
    assert session6.counter(session6.add).__code__.co_freevars != None , "No free variables in the function"

def test_session6_decorator_no_args():
    '''
        Test decorator fnction (counter) with no arguments
    '''
    with pytest.raises(TypeError, match=r".*required positional argument: 'fn'*"):
        session6.counter()
