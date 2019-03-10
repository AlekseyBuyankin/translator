
# a = str(input())
a = '( a + d ) / c + b * ( e + d )'
b = 'a d + c / b e d + * +'
list = list(a.split(' '))

print(list)

print()
outList = []
for i in list:
    stack = []
    if i == '(':
        if isinstance(i, str):
            outList.append(i)
