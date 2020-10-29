def max_profit(prices): # brute-force
    tot_max = 0
    current_max = 0
    for m in range(0, len(prices)-1):
        buy_price = prices[m]
        for n in range(m+1, len(prices)):
            if prices[n] > buy_price:
                sell_price = prices[n]
                current_max = sell_price - buy_price
                # print(current_max)
                if current_max > tot_max:
                    tot_max = current_max
    print(tot_max)
    return tot_max

def max_profit2(prices): # dynamic programming by diff table
    max_profit = 0
    if len(prices) < 2:
        return max_profit

    profit_diff_table = [prices[m]-prices[m-1] for m in range(1, len(prices))]
    max_profit = max(max_profit, profit_diff_table[0])
    if len(profit_diff_table) == 1:
        return max(max_profit, profit_diff_table[0])
    for i in range(1, len(profit_diff_table)):
        if profit_diff_table[i-1] > 0:
             profit_diff_table[i] += profit_diff_table[i-1]
        if profit_diff_table[i] > max_profit:
            max_profit = profit_diff_table[i]
    return max_profit






print(max_profit2([1, 4, 2]))
print(max_profit2([1, 2]))
# max_profit2([1,2])
