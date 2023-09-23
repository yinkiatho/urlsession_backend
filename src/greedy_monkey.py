import json
from typing import Dict, List
import re
import sys

input = {
    "w": 100,
    "v": 150,
    "f": [
        [60, 70, 60],
        [30, 80, 40],
        [35, 70, 70],
        [50, 100, 50],
    ]
}
input2 = {
    "w": 100,
    "v": 150,
    "f": [
        [110, 80, 60],
        [80, 155, 90]
    ]
}


def max_value(obj):
    maxWeight = obj["w"]
    volume = obj["v"]
    fruits = obj["f"]

    basket = {}

    def getTotalVolume(basket):
        return sum(basket[key][1] for key in basket)

    def getTotalWeight(basket):
        return sum(basket[key][0] for key in basket)

    for weight, vol, value in fruits:
        if vol > volume or weight > maxWeight and not basket:
            continue

        if (getTotalVolume(basket) + vol <= volume) and (getTotalWeight(basket) + weight <= maxWeight):
            idx = len(basket)
            dict_key = "f." + str(idx)
            basket[dict_key] = [weight, vol, value]

        else:
            # Sort the basket by fruit value in descending order
            sorted_basket = sorted(
                basket.items(), key=lambda x: x[1][2], reverse=True)

            for key, (basket_weight, basket_vol, basket_value) in sorted_basket:
                if (getTotalVolume(basket) - basket_vol + vol <= volume) and (getTotalWeight(basket) - basket_weight + weight <= maxWeight):
                    # Calculate the new total value with the replacement
                    new_total_value = sum(basket[k][2]
                                          for k in basket) - basket_value + value

                    if new_total_value > sum(basket[k][2] for k in basket):
                        # Replace the fruit in the basket
                        del basket[key]
                        dict_key = "f." + str(len(basket))
                        basket[dict_key] = [weight, vol, value]
                        break

    # Calculate the final total value in the basket
    final_total_value = sum(basket[key][2] for key in basket)

    return final_total_value


def max_fruit_value(w, v, f):
    n = len(f)

    # Initialize a 3D DP table to store the maximum value
    dp = [[[0] * (v + 1) for _ in range(w + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, volume, value = f[i - 1]
        for weight_limit in range(w + 1):
            for volume_limit in range(v + 1):
                # Initialize the value to the previous row's value
                dp[i][weight_limit][volume_limit] = dp[i -
                                                       1][weight_limit][volume_limit]

                # Check if the current fruit can be included
                if weight <= weight_limit and volume <= volume_limit:
                    dp[i][weight_limit][volume_limit] = max(
                        dp[i][weight_limit][volume_limit],
                        dp[i - 1][weight_limit -
                                  weight][volume_limit - volume] + value
                    )

    # The maximum value is in the last cell of the DP table
    return dp[n][w][v]

def maxValue(obj):
    #print(obj)
    maxWeight = obj["w"]
    volume = obj["v"]
    fruits = obj["f"]
    
    basket = {}
    
    def getTotalVolume(basket):
        total = 0
        for key in basket:
            total += basket[key][1]
        return total

    def getTotalWeight(basket):
        total = 0
        for key in basket:
            total += basket[key][0]
        return total

    
    counter = 0
    for weight, vol, value in fruits:
        
        if vol > volume or weight > maxWeight and len(basket) == 0:
            continue
        
        #check total volume can fit in basket if can just add
        elif getTotalVolume(basket) + vol < volume and getTotalWeight(basket) + weight < maxWeight:
            idx = counter
            dict_key = "f." + str(idx)
            basket[dict_key] = [weight, vol, value]
            counter += 1
        
        #total volume cannot fit in basket, check if can replace any current fruit with new fruit
        else:
            for i in range(len(basket)):
                dict_key = "f." + str(i)
                if basket[dict_key][2] < value and getTotalVolume(basket) - basket[dict_key][1] + vol < volume and getTotalWeight(basket) - basket[dict_key][0] + weight < maxWeight:
                    basket.remove(dict_key)
                    basket["f." + str(counter)] = [weight, vol, value]
                    break
                
    return sum([basket[key][2] for key in basket])
                
#print(max_fruit_value(input["w"], input["v"], input["f"]))  
if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: python my_script.py <JSON data>")
        sys.exit(1)

    # Parse the JSON data from the command line argument
    json_data = sys.argv[1]
    #print(json_data)
    try:
        data = json.loads(json_data)
        result = max_fruit_value(data)
        print(result)  # Print the result to stdout
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
            
            
        
        
        
        
        
    