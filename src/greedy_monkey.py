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
        [35, 70, 70]
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

def maxValue(obj):
    print(obj)
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
        
        if vol > volume or weight > maxWeight:
            continue
        
        #check total volume can fit in basket if can just add
        if getTotalVolume(basket) + vol < volume and getTotalWeight(basket) + weight < maxWeight:
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
                
                
if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: python my_script.py <JSON data>")
        sys.exit(1)

    # Parse the JSON data from the command line argument
    json_data = sys.argv[1]
    print(json_data)
    try:
        data = json.loads(json_data)
        result = maxValue(data)
        print(result)  # Print the result to stdout
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
            
            
        
        
        
        
        
    