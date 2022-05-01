
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

'''+------+-------+----------------+
round4
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+

'''
def main():
    checkout('abcd')

#unittests in test_checkout_solution.py file in same folder

def checkout(skus):
    #create array for prices
    #convert all strings tolower for consistency
    #assuming input is a string of letters, without spaces or commas
    #if the counter dict reaches 3 items for a or b, take a discount off the total prices, and reset the counter for that letter
    #check it is a string

    #Round 2
    #add new item E
    #check that whatever offer is given is the lowest
    #getting a B for free when you buy 2 Es would not affect the total I don't think, because that would be strange

    #Round 4
    # update the counter dict first, then work off of the counter dict

    total = 0
    prices = {'A':50,
    'B':30,
    'C':20,
    'D':15,
    'E':40,
    'F':10,
    'G':20,
    'H':10,
    'I':35,
    'J':60,
    'K':80,
    'L':90,
    'M':15,
    'N':40,
    '0':10,
    'P':50,
    'Q':30,
    'R':50,
    'S':30,
    'T':20,
    'U':40,
    'V':50,
    'W':20,
    'X':90,
    'Y':10,
    'Z':50}

    if skus == "":
        return total
    if not skus.isalpha():
        return -1

    # cleanedSkus = skus.lower().strip()

    counter = Counter(skus)
    newCounter = updateCounterDict(counter)

    for key,value in newCounter.items():
        if key == 'A':
            total += totalValueOfAs(newCounter[key])
        elif key == 'B':
            total += totalValueOfBs(newCounter[key])
        elif key == 'H':
            #5H for 45, 10H for 80 
            tens = newCounter[key] // 10
            remTens = newCounter[key] % 10
            fives = remTens // 5
            remainder = remTens % 5
            total += (tens * 80) + (fives * 45) + (remainder * prices[key])
        elif key == 'K':
            #2K for 150
            bundles =  newCounter[key] // 2
            remainder = newCounter[key] % 2
            total += (bundles * 150) + (remainder * prices[key])
        elif key == 'P':
            #5P for 200 
            bundles =  newCounter[key] // 5
            remainder = newCounter[key] % 5
            total += (bundles * 200) + (remainder * prices[key])
        elif key == 'Q':
            #3Q for 80
            bundles =  newCounter[key] // 3
            remainder = newCounter[key] % 3
            total += (bundles * 80) + (remainder * prices[key])
        elif key == 'V':
            #2V for 90, 3V for 130 
            threes = newCounter[key] // 3
            remThrees = newCounter[key] % 3
            twos = remThrees // 2
            remainder = remThrees % 2
            total += (threes * 130) + (twos * 90) + (remainder * prices[key])
        else:
            total += prices[key] * newCounter[key]

    #Special offers
    # total += totalValueOfAs(counter['A'])
    # # # numOfFreeBs = counter['E'] // 2
    # # # totalBs = max(counter['B'] - numOfFreeBs, 0)
    # total += totalValueOfBs(newCounter['B'])
    # total += totalValueOfFs(counter['F'])
    
    return total

def totalValueOfAs(numAs):
    fives = numAs // 5
    remfives = numAs % 5
    threes = remfives // 3
    remainder = remfives % 3
    return (fives * 200) + (threes * 130) + (remainder *50 )

def totalValueOfBs(numBs):
    bundles = numBs // 2
    remainder = numBs % 2
    return (bundles * 45) + (remainder * 30)

def totalValueOfFs(numFs):
    bundles = numFs // 3
    remainder = numFs % 3
    return (bundles * 20) + (remainder * 10)

def updateCounterDict(counterDict):
    for key,value in counterDict.items():
        if key == 'E' and 'B' in counterDict:
            counterDict['B'] = max(counterDict['B'] - counterDict['E'] // 2,0)
        if key == 'F':
            counterDict['F'] -= counterDict['F'] // 3
        if key == 'N' and 'M' in counterDict:
            counterDict['M'] = max(counterDict['M'] - counterDict['N'] // 3,0)
        if key == 'R' and 'Q' in counterDict:
            counterDict['Q'] = max(counterDict['Q'] - counterDict['R'] // 3,0)
        if key == 'U':
            counterDict['U'] -= counterDict['U'] // 4
    return counterDict


if __name__ == "__main__":
    main()





