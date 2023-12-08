#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
5-no_c.py
#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string
