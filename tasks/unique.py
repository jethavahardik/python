# a=['a','b','b','c','b','c']
# s=[]
# count=0
# for i in a:
#     count=count+1
#     if i=='b':
#         s.append(i)
# print(set(s))
a=['a','b','b','c','b','c']
s=[]
count=0
for i in a:
    count=count+1
    if i==set(count):
        s.append(i)
print(s)