import os
print('welcome to secret auction program')

auction_data= {}

def auction():
    more_bidders = True
    heighest_bidder = ''
    while more_bidders == True:
        name = input('what is your name: ')
        bid = int(input('What is your bid: $'))
        auction_data[name] = bid
        bidders = input('are there more bidders? "yes" or "no"').lower()
        if bidders == 'yes':
            more_bidders = True
        else:
            more_bidders = False
        os.system('cls')
        if more_bidders == False:
            heighest_bidder = max(auction_data, key=auction_data.get)
                # print(auction_data[key])
            bid_amount= auction_data[heighest_bidder]
        
    print(f"Winner is {heighest_bidder} with a bid of ${bid_amount}")
    print(auction_data)

auction()    