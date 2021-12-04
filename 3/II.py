#12
#List of strings of binary numbers --> Most Common Value of nth bit (1st bit is defined as the leftmost one)
def MCV(bList,n):
    counter = 0
    for bNumber in bList:
        counter += int(bNumber[n-1])

    if counter >= len(bList)/2: 
        return 1
    else:
        return 0

def LCV(bList,n):
    res = MCV(bList,n)
    if res == 1:
        return 0
    elif res == 0:
        return 1

#iteratively delete member of list if they don't meet condition from fun
def bListFilter(bList,fun):
    i = 0
    while len(bList) > 1:
        res = fun(bList,i+1)
        print(res, bList, i+1)
        for bNum in list(bList): #Make copy so we can remove during interation
            if int(bNum[i]) != res:
                bList.remove(bNum)
        i += 1
    return bList

#binary string to decimal number
def bStringToDec(bString):
    bits = len(bString)
    res = 0
    for i,b in enumerate(bString):
        res += int(b)*2**(bits-i-1)
    return res



bList = []
with open("input.txt",'r') as file:
    for line in file:
        bList.append(line.rstrip())

O2_list = bList[:]
CO2_list = bList[:]
O2_list = bListFilter(O2_list,MCV)
CO2_list = bListFilter(CO2_list,LCV)
print(O2_list, CO2_list)
O2_rating = bStringToDec(O2_list[0])
CO2_rating = bStringToDec(CO2_list[0])
print(f"O2:{O2_rating}\nCO2:{CO2_rating}\nLife support rating:{O2_rating*CO2_rating}")



