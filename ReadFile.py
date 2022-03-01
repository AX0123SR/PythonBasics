"""
- Open the file in read mode
- Read the content from the file
- reverse the file
- Again open the file in write mode
- write the reversed content again into the file
"""

with open("test.txt",'r') as file:
    content = file.readlines()
    reversed(content)
    with open("test.txt",'w') as writer:
        for line in reversed(content):
            writer.write(line)
