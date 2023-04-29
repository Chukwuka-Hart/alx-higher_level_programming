#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


if __name__ == "__main__":
    import sys
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        arg_list = load("add_item.json")
    except FileNotFoundError:
        arg_list = []
    arg_list.extend(sys.argv[1:])
    save(arg_list, "add_item.json")
