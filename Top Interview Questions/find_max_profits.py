def find_max_profits(prices) -> int:
    if not prices:
            return 0
    max_profits = 0
    current_loweset_price = prices[0]
    for day in range(1, len(prices)):
        current_profit = prices[day] - current_loweset_price
        if current_profit > 0:
            max_profits += current_profit
            current_loweset_price = prices[day]
        else:
            current_loweset_price = prices[day]
    return max_profits
