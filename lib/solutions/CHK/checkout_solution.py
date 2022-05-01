
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
        if letter in prices:
            total += prices[letter]
        else:
            return -1
    
    #offers
    if counter['A'] // 3 > 0:
        discount = (counter['A'] // 3) * 20
        total -= discount
    if counter['B'] // 2 > 0:
        discount2 = (counter['B'] // 2) * 15
        total -= discount2
    
    return total

if __name__ == "__main__":
    main()

