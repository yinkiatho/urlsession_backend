import json
from typing import Dict, List
import re
doc = {
    "classes": [
        {
            "Order": {
                "orderId": "String",
                "version": "Long",
                "orderType": "OrderType",
                "orderSide": "OrderSide",
                "status": "Status",
                "allocations": "List<Allocation>"
            },

            "OrderType": [
                "MarketOrderType",
                "LimitOrderType"
            ],
            "MarketOrderType": "",
            "LimitOrderType": {
                "price": "Double"

            },
            "OrderSide": [
                "Buy",
                "Sell"
            ],
            "Status": [
                "New",
                "Verifying",
                "Pending",
                "Working",
                "PartiallyFilled",
                "Filled",
                "Cancelled"
            ],
            "Allocation": [
                "LongAllocation",
                "EmptyAllocation"
            ],
            "LongAllocation": {
                "clientName": "String"
            },
            "EmptyAllocation": ""
        }],
    "statements": [
        "Order.",
        "Order.order",
        "Order.allocations.",
        "Status.P",
        "MarketOrderType."
    ]
}


def getNextProbableWords(classes: List[Dict],
                         statements: List[str]) -> Dict[str, List[str]]:
    #print("here")
    # Create a dictionary to store the class mappings
    class_dict = {}
    print(classes)
    for class_obj in classes:
        class_dict.update(class_obj)
    # print(class_dict)

    # Create a dictionary to store the results
    results = {}

    # Helper function to find probable words for a statement
    def find_probable_words(statement):
        words = statement.split('.')
        num_dots = statement.count('.')
        # add dots in between words

        # current_class = class_dict.get(curr_word, None)

        while (results.get(statement, None) is None and len(words) > 1 and num_dots > 0):
            curr_word = words[0]
            current_class = class_dict.get(curr_word, None)
            if current_class is None:
                results[statement] = [""]
                break

            if current_class is not None:
                if isinstance(current_class, str):
                    # Case 1: Empty class
                    #print("here str")
                    results[statement] = [""]
                elif isinstance(current_class, dict):
                    # Case 2: Class containing key-value pairs
                    #print("here dict")
                    # Case 2a: Class containing key-value pairs
                    if len(words) == 2 and num_dots == 1:
                        next_word = words[1]
                        #print("here dict 1")

                        probable_words = [
                            key for key in current_class.keys() if key.startswith(next_word)]
                        results[statement] = sorted(probable_words)[:5]
                        num_dots -= 1
                    else:
                        #print("here dict 2")
                        num_dots -= 1
                        words = words[1:]

                elif isinstance(current_class, list):

                    # Case 3: List of strings (enum or polymorphic type)
                    if len(words) == 2 and num_dots == 1:
                        next_word = words[1]
                        probable_words = [
                            item for item in current_class if item.startswith(next_word)]
                        results[statement] = sorted(probable_words)[:5]
                        num_dots -= 1

                    else:
                        results[statement] = []

    # Process each statement
    for statement in statements:
        find_probable_words(statement)
    #print(results)
    return results

print(getNextProbableWords(doc["classes"], doc["statements"]))
# Example usage with generic JSON data and statements
# print(json.dumps(result, indent=2))
