def greedy(coins: list, targetValue: int):
    # Sort coins in descending order for greedy selection
    coins.sort(reverse=True) # always count the largest count first.
    
    track = 0
    addList = []
    
    for coin in coins:
        while track + coin <= targetValue:
            track += coin
            addList.append(coin)  # Add the chosen coin
    
    return addList

def main():
    testCoins = [1, 3, 5, 7,8]
    testValue = 10
    listAddCoins = greedy(testCoins, testValue)
    print(listAddCoins)

if __name__ == "__main__":
    main()
