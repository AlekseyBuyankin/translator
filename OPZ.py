import re
import string

from defs import expression, outputUntil

a3 = '''
        program hello ; 
        label m1 , m2 ; 
        const N = 10 ; 
        var a , b : real ; 
        s : string ; 
        function pepega ( e , z : integer ; var x , m : string ) : integer;
        var zz : integer ; 
        begin 
        m := 'LHS' ; 
        end ;
        begin 
        pepega(e,z,x,m); 
        m1: a := 5.65E+4; 
        if(a > 6)then 
        s := 'MHS' 
        else 
        s := 'VHS'; 
        goto m1; 
        end.
        '''
a4 = '''
        hello program 
        m1 m2 label 
        N 10 = const
        a b : real var
        s : string
        pepega e z : 2 integer КО x m : 2 string var КО НП
        zz : integer var КО
        m 'LHS' :=
        КП
        НТ
        pepega e z x m
        m1 : a 5.65E+4 :=
        a 6 > M1 УПЛ 
        s 'MHS' := M2 БП
        M1 : s 'VHS' := M2 :
        m1 БП
        КТ
        '''
a1 = ''
a5 = '''
W0 S0 R4 R11 
W6 I0 R1 I1 R4 R11 
W2 I2 O7 N0 R4 R11 
W1 I3 R1 I4 R3 W4 R4 R11 
I5 R3 W5 R4 R11 
W10 I6 R5 I7 R1 I8 R3 W3 R4 W1 I9 R1 I10 R3 W5 R6 R3 W3 R4 R11 
W1 I11 R3 W3 R4 R11 
W11 R11 
I10 O8 S1 R4 R11 
W16 R4 R11 
W11 R11 
I6 R5 I7 R1 I8 R1 I9 R1 I10 R6 R4 R11 
I0 R3 I3 O8 N1 R4 R11 
W13 R5 I3 O6 N2 R6 W14 R11  
I5 O8 S2 R11 
W15 R11 
I5 O8 S3 R4 R11  
W12 I0 R4 R11  
W17 R11'''

for i in a5:
    if i != '\n':
        a1 += i
a2 = ''
a6 = '''
S0 W0 
I0 I1 W6 
I2 N0 O7 W2 
I3 I4 R3 2 W4 W1 КО 
I5 R3 W5 
I6 I7 I8 R3 2 W3 I9 I10 R3 2 W5 W1 КО R3 W3 НФ 
I11 R3 W3 W1 КО 
I10 S1 O8 
КФ 
НТ 
I6 I7 I8 I9 I10 
I0 R3 I3 N1 O8 
I3 N2 O6 M1 УПЛ 
I5 S2 O8 M2 БП 
M1 R3 I5 S3 O8 M2 R3 
I0 БП 
КТ'''
for i in a6:
    if i != '\n':
        a2 += i

inputList = list(a1.split(' '))
exampList = list(a2.split(' '))

stack = []
outputList = []
priorityList = []
isLetterOrNumber = '[a-zA-Z0-9]'.format(re.escape(string.punctuation))

# переменные для массивов
isBracket = False
AM = '2АЭМ'

# переменные для функции
isFunc = False
F = 'W10'
counterF = 0

# переменные для if/then/else
isIF = False
isElse = False  # для определения полного и неполного условного оператора
M1 = 'M1'
M2 = 'M2'
UPL = 'УПЛ'
BP = 'БП'

# переменные для GOTO
isGOTO = False

w = ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12', 'W13', 'W14', 'W15', 'W16', 'W17',
     'W18']
separator = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11']
operators = ['O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10']
isProgram = False
isLabel = False
isConst = False
isVar = False
isType = False
isProc = False
isOpenBracket = False
isSemicolon = False
isProcActive = False
isFuncActive = False
isBeginProcFunc = False
isBody = False
isEND = False
typeCounter = 0  # счетчик операндов

for i in inputList:
    print(i)
    print('out  ', outputList)
    print('stack', stack)
    print('prior', priorityList)
    print('typeCounter', typeCounter)
    print()

    if re.match(isLetterOrNumber, i) and not (i in w) and not (i in separator) and not (i in operators):
        outputList.append(i)
        if isSemicolon:
            isSemicolon = False
            typeCounter = 1

    # (
    if i == 'R5':
        print('-  (  -')
        if not isProc:
            priorityList.append(0)
            stack.append(i)
        if isProc:
            isOpenBracket = True
            typeCounter = 1

    # )
    if i == 'R6':
        print('-  )  -')
        if not isType:
            outputList, stack, priorityList = outputUntil(['R5', 'R1', 'W14', 'W15'], outputList, stack, priorityList)

        if isProc:
            isOpenBracket = False
            if not isVar:
                outputList.append('КО')

        if isVar:
            isVar = False
            isType = False
            outputList.append('W1')
            outputList.append('КО')

    # [
    if i == 'R7':
        print('-  [  -')
        priorityList.append(0)
        stack.append(i)
        isBracket = True

    # ,
    if i == 'R1' and isBracket:
        AM = '3АЭМ'
        outputList, stack, priorityList = outputUntil(['R7'], outputList, stack, priorityList)
        priorityList.append(1)
        stack.append(i)

    if i == 'R1' and isVar:
        typeCounter += 1

    if i == 'R1' and isProc and not isVar:
        print('isProc:', isProc)
        typeCounter += 1

    # ]
    if i == 'R8':
        print('-  ]  -')
        n = len(stack)
        for j in range(0, n):
            print(stack[-1])
            print('out  ', outputList)
            print('stack', stack)
            print('prior', priorityList)
            print()
            if stack[-1] != 'R1':
                del priorityList[-1]
                outputList.append(stack[-1])
                del stack[-1]
            else:
                print(',')
                del priorityList[-1]
                del stack[-1]
                print('out  ', outputList)
                print('stack', stack)
                print('prior', priorityList)
                print()
                break
            print('out  ', outputList)
            print('stack', stack)
            print('prior', priorityList)
            print()

        outputList.append(AM)
        AM = '2АЭМ'
        isBracket = False

    # IF
    if i == 'W13':
        isIF = True
        if len(stack) != 0:
            if stack[-1] == 'R5':
                del priorityList[-1]
                del stack[-1]
        priorityList.append(0)
        stack.append(i)

    # THEN
    if i == 'W14':
        outputList, stack, priorityList = outputUntil(['W13'], outputList, stack, priorityList)
        priorityList.append(1)
        stack.append(i)
        outputList.append(M1)
        outputList.append(UPL)

    # ELSE
    if i == 'W15':
        isElse = True
        outputList, stack, priorityList = outputUntil(['W14'], outputList, stack, priorityList)
        priorityList.append(1)
        stack.append(i)
        outputList.append(M2)
        outputList.append(BP)
        outputList.append(M1)
        outputList.append('R3')

    # ;
    if i == 'R4':
        print('-  ;  -')
        if not isType and not isProc:
            if isIF:
                outputList, stack, priorityList = outputUntil(['W15', 'W14'], outputList, stack, priorityList)
            else:
                n = len(stack)
                print('else')
                for j in range(0, n):
                    print(stack[-1])
                    print('out  ', outputList)
                    print('stack', stack)
                    print('prior', priorityList)
                    print()
                    del priorityList[-1]
                    outputList.append(stack[-1])
                    del stack[-1]
                    print('out  ', outputList)
                    print('stack', stack)
                    print('prior', priorityList)
                    print()

        if isProgram:
            isProgram = False
            outputList.append('W0')

        if isLabel:
            isLabel = False
            outputList.append('W6')

        if isConst:
            isConst = False
            outputList.append('W2')

        if isGOTO:
            isGOTO = False
            outputList.append(BP)

        if isIF:
            if isElse:
                outputList.append(M2)
            else:
                outputList.append(M1)
            outputList.append('R3')
            isIF = False
            isElse = False

        if isProc:
            if isOpenBracket:
                isSemicolon = True
            elif not isOpenBracket:
                isProc = False
                if isFunc:
                    outputList.append('НФ')
                else:
                    outputList.append('НП')
            elif not isVar:
                isType = True

        if isVar:
            isVar = False
            outputList.append('W1')

        if isType:
            isType = False
            outputList.append('КО')

        if isEND:
            print('isEnd:', isEND)
            if isBeginProcFunc:
                print('isBeginProcFunc:', isBeginProcFunc)
                isEND = False
                print('isFuncActive:', isFuncActive)
                if isFuncActive:
                    outputList.append('КФ')
                    isFuncActive = False
                elif isProcActive:
                    isProcActive = False
                    outputList.append('КП')

    # program
    if i == 'W0':
        isProgram = True

    # label
    if i == 'W6':
        isLabel = True

    # const
    if i == 'W2':
        isConst = True

    # procedure
    if i == 'W9' or i == 'W10':
        isProc = True
        if i == 'W10':
            isFunc = True
        if not isBody:
            if i == 'W10':
                isFuncActive = True
            else:
                isProcActive = True

    # begin
    if i == 'W11':
        if isProcActive or isFuncActive:
            isBeginProcFunc = True

    # GOTO
    if i == 'W12':
        isGOTO = True

    # :
    if i == 'R3':
        outputList.append('R3')

    # var
    if i == 'W1':
        isType = True
        isVar = True
        if isProc:
            typeCounter = 0
        typeCounter += 1

    # of
    if i == 'W8':
        isType = True

    # real
    if i == 'W4':
        if typeCounter != 0 and typeCounter != 1:
            outputList.append(str(typeCounter))
        outputList.append('W4')
        typeCounter = 0

    # integer
    if i == 'W3':
        if typeCounter != 0 and typeCounter != 1:
            outputList.append(str(typeCounter))
        outputList.append('W3')
        typeCounter = 0

    # string
    if i == 'W5':
        if typeCounter != 0 and typeCounter != 1:
            outputList.append(str(typeCounter))
        outputList.append('W5')
        typeCounter = 0

    # end
    if i == 'W16':
        isEND = True

    # begin (body)
    if i == 'W11' and not isProcActive and not isFuncActive and not isIF:
        isBody = True
        outputList.append('НТ')

    # end.
    if i == 'W17':
        if isBody:
            isEND = False
            outputList.append('КТ')  # конец тела программы

    # описание приоритетов
    outputList, stack, priorityList = expression(i, ['O8'], 2, outputList, stack, priorityList)

    outputList, stack, priorityList = expression(i, ['&'], 3, outputList, stack, priorityList)

    outputList, stack, priorityList = expression(i, ['O5', 'O6', 'O7', 'O9', 'O10', 'O11'], 5, outputList, stack,
                                                 priorityList)

    outputList, stack, priorityList = expression(i, ['O0', 'O1'], 6, outputList, stack, priorityList)

    outputList, stack, priorityList = expression(i, ['O2', 'O3'], 7, outputList, stack, priorityList)

    outputList, stack, priorityList = expression(i, ['O4'], 8, outputList, stack, priorityList)

    print('out   ', outputList)
    print('Ответ:', exampList)
    print('stack', stack)
    print('prior', priorityList)
    print('typeCounter', typeCounter)
    print()

print('-------------------')
print('Входной список: ', inputList)
print()
print('Выходной список:', outputList)
print('Ответ:          ', exampList)
if exampList == outputList:
    print('True')
else:
    print('False')
