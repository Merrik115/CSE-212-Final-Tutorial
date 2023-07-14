def calculate_total(bought_stack, bought, price, sold, total):
    for x in range(0, bought):
        bought_stack.append(price)
    
    for x in range(0, sold):
        total = total + bought_stack.pop()
        

    return total


bought_stack = []
bought = [5, 10, 6, 4, 8, 6]
price = [100, 125, 150, 175, 200, 225]
sold = [3, 6, 9, 5, 5, 7]
total = 0

for x in range(0, len(bought)):
    total = calculate_total(bought_stack, bought[x], price[x], sold[x], total)
    

print("The total amount made is $", total)
