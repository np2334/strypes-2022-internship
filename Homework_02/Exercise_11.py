import sys

# 53 - 1 = 52 голяма разлика, 53 - 50 = 3 най-малка разлика, т.е. това ми трябва
def get_smallest_difference_coin_index(total, availableValuesOfCoins):
    smallestDifference = sys.maxsize
    smallestDifferenceCoinIndex = -1

    for i in range(0, len(availableValuesOfCoins)):
        currentValue = availableValuesOfCoins[i]
        currentDifference = total - currentValue

        # стойността на монетата е по-голяма от сумата, т.е. 53 - 100 = негативно число, пропускам итерацията 
        if currentDifference < 0:
            continue

        if currentDifference < smallestDifference:
            smallestDifference = currentDifference
            smallestDifferenceCoinIndex = i

    return smallestDifferenceCoinIndex


def calculate_coins(sum):
    availableValuesOfCoins = [100, 50, 20, 10, 5, 2, 1]
    neededCoins = {
        1: 0,
        2: 0,
        5: 0,
        10: 0,
        20: 0,
        50: 0,
        100: 0
    }   

    # първо пробвах като float да изкарвам числата, логически се получи, но бях забравил, че числата с плаваща запетая не са точни, и когато изкарах 0.02 пт 0.03 не получих 0.01
    sum *= 100
    # за да не излиза 1.00 примерно а 1
    sum = int(sum)

    while sum != 0:
        wantedCoinIndex = get_smallest_difference_coin_index(sum, availableValuesOfCoins)
        wantedCoin = availableValuesOfCoins[wantedCoinIndex]

        while sum - wantedCoin >= 0:
            sum -= wantedCoin
            neededCoins[wantedCoin] += 1

    return neededCoins

print(calculate_coins(0.53))
print(calculate_coins(8.94))
print(calculate_coins(0.15))
print(calculate_coins(0.38))