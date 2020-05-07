"""
When we are done with file, the cursor goes to the end of the line so nothing left to read, then we use 'seek(0)' to
move the cursor to the beginning

default mode is 'r' - read a file
'w' - write into a file and also overwrite
'a' - append to a file (previous content is not overwritten)
'r+' - read and write into a file (it does not not create a new file like'w' and 'a' also previous content is
overwritten)

"""
file = open("intro.txt")

print(file.read())
file.seek(0)

print(file.read())
file.seek(0)

print(file.readline())
file.seek(0)

print(file.readlines())  # Gives us a list
file.seek(0)

file.close()

# if you dont want to 'close' file then use:

with open("intro.txt") as file:
    print(file.read())

# Write to files

with open("num.txt", "w") as file:
    file.write('1\n')
    file.write('2\n')
    file.write('3')


# Copying contents of a file into a new file

def copy():
    with open("math.txt") as math:
        text = math.read()

    with open("math2.txt", "w") as math2:
        math2.write(text)


copy()


# Copying contents of a file into a new file and reversed

def copy():
    with open("math.txt") as math:
        text = math.read()

    with open("math2.txt", "w") as math2:
        math2.write(text[::-1])


copy()


# Find and replace

def find_and_replace():
    with open("math.txt", "r+") as math:
        text = math.read()
        new_text = text.replace('10', '100')
        math.seek(0)
        math.write(new_text)


find_and_replace()
