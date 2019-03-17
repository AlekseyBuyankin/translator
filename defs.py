def expression(i, l, value, outputList, stack, priorityList):
    if i in l:
        if len(priorityList) == 0:
            priorityList.append(value)
            stack.append(i)
        else:
            if priorityList[-1] < value:
                priorityList.append(value)
                stack.append(i)
            else:
                del priorityList[-1]
                outputList.append(stack[-1])
                del stack[-1]
                for j in priorityList:
                    if j >= value:
                        del priorityList[-1]
                        outputList.append(stack[-1])
                        del stack[-1]
                    else:
                        break
                priorityList.append(value)
                stack.append(i)

    allList = []
    allList.append(outputList)
    allList.append(stack)
    allList.append(priorityList)

    return allList


def outputUntil(untilList, outputList, stack, priorityList):
    n = len(stack)
    for j in range(0, n):
        print(stack[-1])
        print('out  ', outputList)
        print('stack', stack)
        print('prior', priorityList)
        print()
        if not (stack[-1] in untilList):
            del priorityList[-1]
            outputList.append(stack[-1])
            del stack[-1]
        else:
            print(stack[-1])
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

    allList = []
    allList.append(outputList)
    allList.append(stack)
    allList.append(priorityList)

    return allList
