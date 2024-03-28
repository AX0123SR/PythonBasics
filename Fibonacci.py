a,b=0,1
for i in range(1,9):
    c = a+b
    a=b
    b=c
print(b)


my_list = [i for i in range(1,10) ]
print(my_list)

my_dict={i:4 for i in range(1,6)}
print(my_dict)

t = (1,4,2,25,5,1,2,3,1)
print(t.count(1))

# names = ["Jacob", "Joe", "Jim"]
#
# if (name := input("Enter a name: ")) in names:
#     print(f"Hello, {name}!")
# else:
#     print("Name not found.")

str1 = 'Ayush Sri'
substr = 'yu'

# Print original string and substring
print("Original string is:", str1)
print("Substring is:", substr)

# Sse startswith() and list comprehension
# Find all occurrences of a substring within a string
result = [i for i in range(len(str1)) if str1.startswith(substr, i)]

# Print the number of substring occurrences
print("Number of substring occurrences is:", len(result))
