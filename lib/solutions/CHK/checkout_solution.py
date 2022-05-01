
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

'''+------+-------+----------------+
round 2
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+

round 3
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
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
    'E':40}

    if skus == "":
        return total
    if not skus.isalpha():
        return -1

    # cleanedSkus = skus.lower().strip()

    counter = Counter(skus)

    for letter in skus:
        if letter == 'A':
            continue
        if letter == 'B':
            continue
        if letter == 'F':
            continue
        if letter in prices:
            total += prices[letter]
        else:
            return -1
    
    #Special offers

    total += totalValueOfAs(counter['A'])
    numOfFreeBs = counter['E'] // 2
    totalBs = max(counter['B'] - numOfFreeBs, 0)
    total += totalValueOfBs(totalBs)
    total += totalValueOfFs(counter['F'])
    
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
    pass

if __name__ == "__main__":
    main()




