def coin_change(coins, amount):
    if amount == 0:
        return 0
    coins.sort()
    coins_change_table = {coin: [-1 for j in range(amount+1)] for coin in coins}

    for k, coins_change_list in coins_change_table.items():
        if k == coins[0]:
            for i, v in enumerate(coins_change_table[k]):
                if i < k:
                    continue
                if i % k == 0:
                    coins_change_table[k][i] = i // k
        else:
            for i, v in enumerate(coins_change_table[k]):
                prev_k = coins[coins.index(k) - 1]
                if i < k:
                    coins_change_table[k][i] = coins_change_table[prev_k][i]
                elif i == k:
                    coins_change_table[k][i] = 1
                else:
                    current_coin_num = 0
                    if coins_change_table[k][i] == -1:
                        prev_i = i - k
                        current_coin_num += 1
                        if coins_change_table[k][prev_i] != -1:
                            current_coin_num += coins_change_table[k][prev_i]
                            coins_change_table[k][i] = current_coin_num
                            if coins_change_table[prev_k][i] != -1:
                            # if current_coin_num == 9:
                                # print(coins_change_table[prev_k][i])
                                coins_change_table[k][i] = min(coins_change_table[prev_k][i], current_coin_num)
                            else:
                                coins_change_table[k][i] = current_coin_num
                        else:
                            coins_change_table[k][i] = coins_change_table[prev_k][i]
                        # coins_change_table[k][i] = min(coins_change_table[prev_k][i], current_coin_num)
    # print(coins_change_table)
    # print(coins)
    return coins_change_table[coins[-1]][amount]

# print(coin_change([3,11,14,15], 110))
print(coin_change([186,419,83,408], 6249))
