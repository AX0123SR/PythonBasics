import collections

s = "hey ayush you are ayush, I know ayush"
sub = "ayush"
result = [i for i in range(len(s)) if s.startswith(sub,i)]
print(len(result))

str ="Elephante"

res = collections.Counter(str)
print(res)

resu = dict((i,str.count(i)) for i in set(str))
print(resu)


