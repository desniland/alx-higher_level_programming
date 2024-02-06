#!/usr/bin/python3
'''Dwefines a file-writing function'''


def write_file(filename="", text=""):
    '''Write astring to a UTF* file.
    Args:
    filename (str): name of file to write
    text (str): text to write to file
    Returns: The no. of characters written.
    '''
    with open(filename, "w", encoding="utf-8") as f:
        num_chars = f.write(text)
    return (num_chars)
