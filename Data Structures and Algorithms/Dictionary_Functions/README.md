# Dictionaries used to call functions

## Dictionaries can have intresting keys and values.

In python, a function is also an object. You can assign variables to functions and then call a variable.
```py
def foo():
    """Example code"""
x = foo
x()
```  
Actually, on the topic of what you can do with a function. It can be used as a variable in a function too
```py
def bar(func):
    func()
bar(foo)
```

Python dictionaries can also have anything that is hashable as a key. So not just strings but many objects too. In this demo, we use strings as our keys. But here is an example of a nontraditional key
```py
import datetime
example = {}
timeNow = datetime.datetime.now()
example[timeNow] = "This is valid"
print(example)
```  

Python dictionaries can have any object as a value. And since functions are objects, we can assign them into dictionaries. We can then get a value at a given hash and call it.
```py
example['1'] = foo
example['1']()
```

Finally, we want to call these dicts without checking if it a valid key. A common practice in python is to use try and except blocks. Get used to using these blocks. Unlike other languages, it is common place to have these in your code. One major mistake many new programmers make is to `except` on everything. Instead, you should only catch known exceptions. There are many reasons for this but one of the biggest is because you don't want to catch exceptions such as user interupts. If I wanted to kill a program, I would use ctrl+c. But if I catch all exceptions, it wouldn't end the program.
```py
try:
    example['9']()
except (KeyError, TypeError) as e:
    # Key error is when the dict does not have that key in its list. 
    # Type error would be called if the dict has values that are not functions but we try to call it.
    print("Invalid key or type")
```

---
## Why is this useful?  
Imagine if you wanted to do basically the same thing but the only difference was the function being called. Based on some variable, you excecute some other code. Putting it into a dict can make your code more compact and easiear to expand and work with.
```py
if x == 1:
    one()
elif x == 2:
    two()
...
# Can be converted to
funcs[x]()
```

---
## Running this demo

To run the sample code, first clone the repo. 
 > `cd Dictionary_Functions` to get into this folder.   
 > `python dictionaryFunctions.py` to run the demo

---
I hope you learned something. If you want to see what I am up to, check me out at [CoderJoshDK](https://github.com/CoderJoshDK)