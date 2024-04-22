def count_price():
    needs = 1000
    price = 169
    amount = 10
    total_price = needs / amount * price
    current_price = total_price
    
    for i in range(int(needs/100)):
        percent = current_price / 100
        current_price = current_price - percent
        
    return int(current_price)

print(count_price())