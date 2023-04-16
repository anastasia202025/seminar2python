s= int(input())
p= int(input())
for i in range(s):
    if i * (s-i)==p:
       print(i,s-i)