"""
Exception is an event which disrupts the normal flow of execution.
try and except method are used to handle exceptions.
"""
# There are 2 ways to raise Exception

ItemInCart = 0
#if ItemInCart!=2:
 #   raise Exception("Count is not matching..")

# Assert
assert(ItemInCart == 0)


# try:
#     with open("test.txt",'r') as file:
#         file.read()
#
# except:
#     print("No such file present.")

try:
    with open("test.txt",'r') as file:
        file.read()

except Exception as e:
    print(e)

finally:
    print("I will always executed irrespective of pass/fail test case.")