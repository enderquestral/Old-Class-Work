#Alice’s truck can hold 11 boxes and she charges $200 per trip. 
#Bob’s truck can hold 14 boxes and he charges $250 per trip.
def cheapest(numboxes):
    bobprice = 0
    aliceprice = 0
    placeholder = numboxes

    while placeholder >0: #Alice
        placeholder = placeholder - 11
        aliceprice = aliceprice + 200
    placeholder = numboxes
    while placeholder >0: #Bob
        placeholder = placeholder - 14
        bobprice = bobprice + 250

    if bobprice < aliceprice:
        return "Bob"
    else:
        return "Alice"
