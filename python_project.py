
stock = {}

with open('stock.txt') as fileobj:
  for line in fileobj:
      key, value = line.split(":")
      stock[key] = int(value)

print("Hello and Welcome To The System!!")
print("")

def options():
    print("Press '1' to add stock ")
    print("Press '2' to remove stock")
    print("Press 'c' to check stock")
    print("Press 'd' to delete stock")
    print("Press 'q' to quit the program")
    return input("What would you like to do? ")

def write():
    f = open("stock.txt","w")
    for i in stock :
        f.write( "{}:{}\n".format(i, stock[i]) )
    f.close()

print("List of the current stock:")
for key, value in stock.items():
    print("{}: {}".format(key, value))
# for stocks in stock_file.readlines():
#     print("{}".format(stocks))
print("")
run = options()


while True:
    if run == '1':
        print("")
        addStock = input('Add item: ').lower()
        try:
            amount = int(input('Qty: '))
            if addStock in stock:
                prevAmount = stock[addStock]
                amount += prevAmount

            stock[addStock] = amount
            print("")
            run = options()

            write()

        except ValueError:
            print("Please enter a number")

    elif run == '2':
        print("")
        removeStock = input('Remove item: ').lower()
        try:
            amount = int(input('Qty: '))
            if removeStock in stock:
                prevAmount = stock[removeStock]
                if prevAmount == 0:
                    print('\n{}{}'.format(removeStock, " is not in stock"))
                elif amount > prevAmount:
                    print('\n{}\n{}{} \nplease try again'.format(
                        "Exceed stock limit", "The available stock is ", prevAmount))
                    continue
                else:
                    amount = prevAmount-amount
                    stock[removeStock] = amount

            else:
                print('\n{}{}'.format(removeStock, " is not in stock"))

            print("")
            run = options()

            write()
            
        except ValueError:
            print("Please enter a number")

    elif run =='d':
        print('')
        delStock = input('Delete item: ').lower()
        if delStock in stock :
            del stock[delStock]
            print(delStock, " has been deleted\n")
        else:
            print('{}{}\n'.format(delStock, " is not in stock"))
        write()
        run = options()


    elif run == 'c':
        print("")
        for key, value in stock.items():
            print("{}: {}".format(key, value))
        print("")
        run = options()

    elif run == 'q':
        
        break

    else:
        print("\nIncorrect option !!\n")
        run = options()
