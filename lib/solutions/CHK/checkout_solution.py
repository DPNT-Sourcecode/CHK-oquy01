
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string

'''+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15  
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
    prices = {'a':50,
    'b':30,
    'c':20,
    'd':15}

    cleanedSkus = skus.lower().trim()
    counter = Counter(skus)

    for letter in cleanedSkus:
        if letter in prices:
            total += prices[letter]
        else:
            return -1
    
    #offers
    if counter['a'] // 3 > 0:
        




if __name__ == "__main__":
    main()


