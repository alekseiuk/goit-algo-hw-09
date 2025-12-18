def find_coins_greedy(coins, amount):

    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin 
            if count > 0:
                result[coin] = count
                amount = amount - (coin * count)
    
    return result


def find_min_coins(coins, amount):

    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    
    used_coins = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    used_coins[i] = coin
    
    result = {}
    current_sum = amount
    
    if min_coins[amount] == float('inf'):
        return {}
        
    while current_sum > 0:
        coin = used_coins[current_sum]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_sum -= coin
        
    return result



coins = [50, 25, 10, 5, 2, 1]
amount = 113
    
greedy_res = find_coins_greedy(coins, amount)
print("Greedy algorithm:", greedy_res)

dp_res = find_min_coins(coins, amount)
print("Dynamic programming:", dp_res)