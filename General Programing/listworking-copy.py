months = "JanFebMarAprMayJunJulAugSepOctNovDec"
monthlist = []
def functmain(n):
    for i in range(1, len(months)+1):
            if i%3 == 0:
                    monthlist.append(months[i-3:i])
    return (monthlist[n-1])

def getmonth():
    try:
        n = int(input("Enter a month number: "))
        m =functmain(n)
    except IndexError:
        print('this number')
    return (m)
print(getmonth())




