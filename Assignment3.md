def value_of_a_wallet(x1 , x2 , x3 , x4 ,x5) :

    list_one = [x1 , x2 , x3 , x4 , x5 ]
    highestValue = 0
    lowestValue = x4
    totalValue = 0
    dimes = 0

    for x in list_one:
        if(x > highestValue):
            highestValue = x

        if (x < lowestValue):
            lowestValue = x

        totalValue += x

    dimes = totalValue * 10

    print ("The fattest wallet: " , highestValue)
    print ("The skinniest wallet: " , lowestValue)
    print ("The total value of the wallet : " , totalValue)
    print ("All together, the total value of these wallets in dimes: " , dimes)


    value_of_a_wallet(50, 100, 150, 200, 250)

def periodic_table() :

    exit = False
    elementList = []

    while(exit == False):
        elementName = input("Enter a element name: ")
        elementSymbol = input("Enter a element symbol: ")
        elementAtomic_Number = input("Enter a atomic number: ")
        elementRow = input("Enter the row the element belongs in: ")
        elementCol = input("Enter the column the element belongs in: ")

        element = {"name": elementName, "symbol": elementSymbol, "atomic number": elementAtomic_Number,
                   "row": elementRow,
                   "column": elementCol}


        elementList.append(element)

        getBol = input("Do you want to get data about an element (yes or no)")

        if(getBol == "yes"):

            getElement = input("Which element do you want to get data for (symbol): ")

            index = 0

            for x in elementList:
                if(x.get("symbol") == getElement):
                    print ("\n", x.get("name"), "\n", x.get("symbol"), "\n", x.get("atomic number"),
                           "\n", x.get("row"), "\n", x.get("column"))

        exitBol = input("Do you wish to continue (yes or no)")

        if(exitBol == "no"):
            exit = True




    periodic_table()



