def value_of_a_wallet(x1 , x2 , x3 , x4 ,x5) :

    list_one = [x1 , x2 , x3 , x4 , x5 ]
    highestValue = 0
    lowestValue = 0
    totalValue = 0
    dimes = 0

    for x in list_one:
        if(x > highestValue):
            highestValue = x

        if (x < lowestValue):
             lowestValue = x

             totalValue += x

    dimes = totalValue * 10

    print "The fattest wallet: " + highestValue
    print "The skinniest wallet: " + lowestValue
    print "The total value of the wallet : " + totalValue
    print "All together, the total value of these wallets is worth: " + dimes



