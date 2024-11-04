import sys
import os

GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

file_name = "Basic1"

def change_cpp_hpp_names(name):
    try:
        os.rename(file_name + ".hpp", name + ".hpp")
        os.rename(file_name + ".cpp", name + ".cpp")
        print(GREEN + "Basic.hpp and Basic.cpp renamed to " + name + ".hpp and " + name + ".cpp" + RESET)
    except:
        print(RED + "Error renaming Basic.hpp and Basic.cpp" + RESET)

def change_all_string_Fixed_to_name_in_cpp(name):
    file = file_name + ".cpp"
    try:
        with open(file, "r") as f:
            contents = f.read()
            contents = contents.replace("Fixed", name)
            contents = contents.replace("fixed", name.lower())
        with open(file, "w") as f:
            f.write(contents)
        print(GREEN + "All Fixed and fixed replaced with " + name + " in " + file + RESET)
    except:
        print(RED + "Error replacing Fixed and fixed with " + name + " in " + file + RESET)

def change_all_string_Fixed_to_name_in_hpp(name):
    file = file_name + ".hpp"
    try:
        with open(file, "r") as f:
            contents = f.read()
            contents = contents.replace("Fixed", name)
            contents = contents.replace("fixed", name.lower())
            contents = contents.replace("FIXED_HPP", name.upper() + "_HPP")
        with open(file, "w") as f:
            f.write(contents)
        print(GREEN + "All Fixed and fixed replaced with " + name + " in " + file + RESET)
    except:
        print(RED + "Error replacing Fixed and fixed with " + name + " in " + file + RESET)

if __name__ == "__main__":
    inpu = GREEN + "TYPE NAME OF CLASS: " + RESET
    name = input(inpu)

    if not any(char.isupper() for char in name):
        print(RED + "Class name should start with a capital letter" + RESET)
        exit(1)
    if os.path.exists(name + ".hpp") or os.path.exists(name + ".cpp"):
        print(RED + "Files with name " + name + ".hpp or " + name + ".cpp already exists" + RESET)
        exit(1)
    change_all_string_Fixed_to_name_in_cpp(name)
    change_all_string_Fixed_to_name_in_hpp(name)
    change_cpp_hpp_names(name)
