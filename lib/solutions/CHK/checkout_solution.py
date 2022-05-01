
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

'''+------+-------+----------------+
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
'''
def main():
    checkout('abcd')

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
    
    # ModifiedSkus = 0

    # cleanedSkus = skus.lower().strip()

    counter = Counter(skus)

    for letter in skus:
        if letter in prices:
            total += prices[letter]
        else:
            return -1
    
    #Special offers
    if counter['A'] // 3 > 0:
        fives = counter['A'] // 5
        remfives = counter['A'] % 5
        threes = remfives // 3
        discountA = (fives * 50) + (threes * 20)
        total -= discountA
    # if counter['E'] // 2 > 0:
    #     numOfFreeBs = counter['E'] // 2
    #     numOfBsToDiscount = min(counter['B'],numOfFreeBs)
    #     discountE = numOfBsToDiscount * 
    #     total -= 
    
    if counter['B'] // 2 > 0:
        discountB = (counter['B'] // 2) * 15
        total -= discountB
    
    return total

def totalValueOfAs(numAs):

    fives = numAs // 5
    remfives = numAs % 5
    threes = remfives // 3
    remainder = remfives % 3

    bundles = numAs // 2
    remainder = numBs % 2

    return (bundles * 45) + (remainder * 30)

def totalValueOfBs(numBs):
    bundles = numBs // 2
    remainder = numBs % 2
    return (bundles * 45) + (remainder * 30)

if __name__ == "__main__":
    main()





