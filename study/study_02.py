N = int(input())
count = 0
resultN = N

while True :
    if resultN < 10 :
        strN = str(resultN) + '0'
        resultN = resultN + int(strN)
        count = count + 1

    elif resultN >= 10 and resultN <= 99:
        strN = str(resultN)
        N1 = int(strN[0])
        N2 = int(strN[1])

        rastN = N1 + N2
        if len(str(rastN)) == 1:
            pass
        else:
            rastN = str(rastN)[1]

        strN = strN[1] + str(rastN)
        resultN = int(strN)
        count = count + 1

    if N == resultN:
        break
print('{0}'.format(count))

# 1 -> 01
# 10 + 01 -> 11
#
# 11 -> 1+1 -> 2
# '1' + '2' -> '12'
#
# 3 -> 03
# 3 + 33 -> 36