import re
import string

# a = str(input())
a = '( a + d ) / c + b * ( e + d )'
b = 'a d + c / b e d + * +'

c = 'a + b * c'
d = 'a b c * +'

list = list(a.split(' '))

stack = []
outList = []
isBracket = False
priority = 0
nowPriority = 0
isLetter = '[a-zA-Z]'.format(re.escape(string.punctuation))
count = 1

for i in list:
    if i == '(':
        isBracket = True
        nowPriority = 0
    if i == ')':
        isBracket = False
        for j in stack:
            outList.append(j)
            stack = []
    if re.match(isLetter, i):
        outList.append(i)
    if i == '+' or i == '-':
        if nowPriority == 0:
            nowPriority = 6
            priority = 6
        else:
            priority = 6
        if nowPriority > priority:
            for j in stack:
                outList.append(j)
                stack = []
            stack.append(i)
        else:
            stack.reverse()
            stack.append(i)
            stack.reverse()
        nowPriority = priority
    if i == '*' or i == '/':
        priority = 7
        if priority < nowPriority:
            for j in stack:
                outList.append(j)
                stack = []
        stack.reverse()
        stack.append(i)
        stack.reverse()
        nowPriority = priority
    count += 1

for j in stack:
    outList.append(j)

print(a)
print()
print(outList)
