#!/usr/bin/env python
# coding: utf-8

# Write a function print_info(**kwargs) that prints all the key-value pairs passed to it.
# 

# In[2]:


def test(**kwargs):
    return kwargs


# In[4]:


test(a=1,b=2,c=3,d=4,n=[1,2,3,4,5])


# Create a function greet_people(**kwargs) where each key is a person's name and the value is their greeting. Print out a greeting for each person.
# 
# 

# In[6]:


def greet_people(**kwargs):
    return kwargs


# In[10]:


greet_people(Rohit="Hi",virat = "Hi",Rahul="Hello")


# Write a function person_details(name, age, **kwargs) that prints name and age, and then any additional information passed in.
# 

# In[13]:


def people_details(**n):
    return n


# In[15]:


people_details(name="Rohit",age=37,n=["RHB","cricketer"])


# Define a function build_profile(**kwargs) that builds and returns a dictionary of user profile information.
# 

# In[21]:


def build_profile(**kwargs):
    return kwargs
build_profile(Name="Balu",Age=23,Fathername="Ramu")


# Write a function combine_dicts(**kwargs) that takes multiple keyword arguments and returns them as a single dictionary.

# In[37]:


def combine_dicts(**kwargs):
    return kwargs


# In[38]:


combine_dicts(name="jasprit", age=30, city="mumbai")


# Create a function sum_named_numbers(**kwargs) that sums all the values passed as keyword arguments (assume all values are numbers).

# In[31]:


def test2(**kwargs):
    return sum(kwargs.values())
  


# In[33]:


test2(a=1,b=2,c=3)


# Define a function filter_keywords(**kwargs) that only returns keyword arguments where the value is a string.
# 

# In[2]:


def filter_keywords(**kwargs):
        return {key: value for key, value in kwargs.items() if isinstance(value, str)}
filter_keywords(a="alice", b="hi",c=45)


# Write a decorator function debug_info(func) that prints **kwargs passed to any wrapped function.
# 

# In[4]:


def debug_info(func):
    def wrapper(*args, **kwargs):
        print("Debug Info - kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper


# Write a function print_styled_text(text, **styles) that applies style options like bold=True, italic=True, etc., and prints how the text should be styled.

# In[1]:


def print_styled_text(text,**styles):
    applied_styles = [style for style,enabled in styles.items() if enabled]

    if applied_styles :
        style_str = ', ' .join(applied_styles)
        print(f"Text : {text}' | Styles_applied : {style_str}")
    else:
        print(f"Text  : {text}' | No styles applied")


# In[3]:


print_styled_text("I am learning datascience at Aimnxt" , bold=True,italic=True,underline=False)


# Write a function custom_message(**kwargs) where it checks for specific keys like name, time, and location and builds a formatted message if those keys exist.

# In[5]:


def custom_message(**kwargs):
    name = kwargs.get('name')
    time = kwargs.get('time')
    location = kwargs.get('location')
    
    message_part = []
    
    if name:
        message_part.append(f"Hello, {name}")
    if time:
        message_part.append(f"at {time}")
    if location:
        message_part.append(f"in {location}")

    if message_part : 
        message = ' '.join(message_part) + "!"
        print(message)
    else:
        print("No specific message to print")

custom_message(name = "Rohit" , time = "7:30pm", location = "miryalaguda")
custom_message(name = "Balu")
custom_message()


# Write a program that takes user input for two numbers and divides them. Use try-except to catch divide-by-zero errors.

# In[8]:


try:
    n = int(input("enter the number"))
    n1 = int(input("enter the number"))
    c =n/n1
    print(c)
except ZeroDivisionError:
    print("please enter non-zero values")
    


# Create a function that reads an integer from user input. Use try-except to handle invalid (non-integer) input.

# In[12]:


def fun():
    try:
        a=int(input("Enter the number"))
        b=int(input("Enter the number"))
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("Enter non-zero values")
fun()


# Write a function that opens a file by name. Use exception handling to catch the case where the file doesn’t exist.

# In[ ]:





# Write a calculator function that takes two numbers and an operation (+, -, *, /) and handles any potential exceptions (e.g., division by zero, invalid operation).

# In[14]:


def cal(a,b,n):
    try:
        if n=='+':
            c = a+b
            return c
        elif n=='-':
            c=a-b
            return c
        elif n=='*':
            c=a*b
            return c
        elif n=='/':
            c=a/b
            return c
    except  ZeroDivisionError:
        print("please enter non-zero values")
    except InvalidOperation:
        print("Please enter properly")
a = cal(2,1,'+')
print(a)
b= cal(4,3,'-')
print(b)
d=cal(3,4,'*')
print(d)
e=cal(4,2,'/')
print(e)


# Make a function get_list_item(lst, index) that returns the element at the given index. Catch exceptions if the index is out of range.

# In[15]:


def get_list_item(lst,index):
    try:
        return lst[index]
    except IndexError:
        print("Index Is Out Of Range")
lst=[1,2,3,4,5,6]
index=int(input("Enter index: "))
get_list_item(lst,index)


# Write a function called greet that takes a name as input and prints "Hello, [name]!"

# In[17]:


def greet(name):
    print(f"Hello,{name} !")
greet("Rohit")


# Create a function add_numbers that takes two numbers as arguments and returns their sum.

# In[18]:


def add(a,b):
    return a+b
add(4,5)


# Write a function is_even that returns True if a number is even, and False otherwise.

# In[20]:


def even(n):
    return n
if n%2==0:
    print("True")
else:
    print("False")
even(4)


# Define a function factorial that returns the factorial of a given number.

# In[23]:


def fact(n):
    
    if n==1:
        return 1
    else:
        return n*fact(n-1)
fact(6)
    


# Create a function reverse_string that takes a string and returns it reversed.

# In[25]:


def rev(st):
    return st[::-1]
rev("Balu")


# Write a function max_of_three that returns the largest of three numbers.

# In[28]:


def max_of_three(a,b,c):
    if a>b and a>c:
        print("a is  largest number")
    elif b>a and b>c:
        print("b is largest number")
    else:
        print("c is largest")
max_of_three(45,18,7)


# Define a function count_vowels that returns the number of vowels in a string.

# In[29]:


def count_vowels(n):
    a = "aeiouAEIOU"
    c =0 
    for a in n:
        c=c+1
    return c
count_vowels("Balachandu")
        


# Write a function fibonacci(n) that returns the nth Fibonacci number.

# In[33]:


def fibo(n):
    a=0
    b=1
    for i in range (n):
        c = a+b
        print(c,end=" ")
        a=b
        b=c
fibo(5)


# In[ ]:




