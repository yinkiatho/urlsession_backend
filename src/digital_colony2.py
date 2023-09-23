import json
import math
from typing import Dict, List

input = [
    {"generations": 10, "colony": "1000"},
    {"generations": 50, "colony": "1000"},
]

test = {"generations": 4, "colony": "914"}


def generateNextGeneration(colony, memo):

    if colony in memo:
        return memo[colony]

    weight = sum([int(x) for x in colony])
    new_colony = []
    for i in range(len(colony) - 1):
        first, second = int(colony[i]), int(colony[i + 1])
        new = first - second if first > second else 10 - (second - first)
        new_digit = str(new + weight)[-1]
        new_colony.append(str(first))
        new_colony.append(new_digit)
    new_colony.append(colony[-1])

    memo[colony] = "".join(new_colony)
    return "".join(new_colony)


def getTotalWeight(obj, memo):

    output = []
    for o in obj:
        generations, colony = o["generations"], o["colony"]
        for i in range(generations):
            colony = generateNextGeneration(colony, memo)
        result = str(sum([int(x) for x in colony]))
        output.append(str(result))

    return output


memo = {}
print(getTotalWeight(input, memo))
print(getTotalWeight([test], memo))
