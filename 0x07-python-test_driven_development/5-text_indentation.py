#!/usr/bin/python3
"""func module"""



def text_indentation(text):
    """func"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i== ':':
            print(i, end="")
            print("")
        else:
            print(i, end="")
    print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
