import json
from typing import Dict, List
import re
import sys

input = [
    {"generations": 10, "colony": "1000"},
    {"generations": 50, "colony": "1000"}
]

test = {
    "generations": 4,
    "colony": "914"
}   

def getTotalWeight(obj):
    #print(obj)
    
    def generateNextGeneration(colony):
        weight = sum([int(x) for x in colony])
        
        new_colony = []
        
        for i in range(len(colony)):
            
            if i == len(colony) - 1:
                new_colony.append(colony[i])
            
            elif i + 1 <= len(colony) - 1:
                first, second = int(colony[i]), int(colony[i + 1])
                #print(first, second)
                new_colony.append(str(first))
                if first == second:
                    new = 0
                    
                elif first > second:
                    new = first - second
                
                else:
                    new = 10 - (second - first)
            
                new_digit = str(new + weight)[-1]
            #print(new_digit)
                new_colony.append(new_digit)
            #print(new_colony)
            
        #new_colony.append(colony[-1])
        res = "".join(new_colony)
        #print(res)
        #print(res)
        return res
    
    output = []
    for o in obj:
        print(o)
        generations, colony = o["generations"], o["colony"]
        for i in range(generations):
            colony = generateNextGeneration(colony)
        result = str(sum([int(x) for x in colony]))
        output.append(result)
        print(output)
        
    return output

print(getTotalWeight(input))
#print(getTotalWeight(test))
if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: python my_script.py <JSON data>")
        sys.exit(1)

    # Parse the JSON data from the command line argument
    json_data = sys.argv[1]
    #print(json_data)
    #print(json.loads(data))
    try:
        #print(json_data)
        res = []
        data = json.loads(json_data)
        print(getTotalWeight(data))  # Print the result to stdout
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
                    
            
        


