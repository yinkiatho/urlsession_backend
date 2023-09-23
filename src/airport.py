# Simple passenger class
import json
from typing import Dict, List
import re
import sys
test = [
    {
        "id": "fc5fdbc0-551d-4099-b7e6-f59e27b238dc",
        "departureTimes": [40, 42, 50, 69, 34, 50],
        "cutOffTime": 48
    },
    {
        "id": "fc5fdbc0-551d-4099-b7e6-f59e27b238dd",
        "departureTimes": [1, 2, 3, 4, 5, 6],
        "cutOffTime": 48
    },
    {
        "id": "fc5fdbc0-551d-4099-b7e6-f59e27b238de",
        "departureTimes": [1, 2, 3, 4, 5, 6],
        "cutOffTime": 48
    },
    {
        "id": "fc5fdbc0-551d-4099-b7e6-f59e27b238df",
        "departureTimes": [1, 2, 3, 4, 5, 6],
        "cutOffTime": 48
    },
    {
        "id": "fc5fdbc0-551d-4099-b7e6-f59e27b238dg",
        "departureTimes": [1, 2, 3, 4, 5, 6],
        "cutOffTime": 48
    }
]


class Passenger:
    def __init__(self, departureTime):
        self.departureTime = departureTime
        self.numberOfRequests = 0

    def askTimeToDeparture(self):
        self.numberOfRequests += 1
        return self.departureTime

    def getNumberOfRequests(self):
        return self.numberOfRequests


def execute(prioritisation_function, passenger_data, cut_off_time):
    totalNumberOfRequests = 0
    passengers = []

    # Initialise list of passenger instances
    for i in range(len(passenger_data["departureTimes"])):
        passengers.append(Passenger(passenger_data["departureTimes"][i]))

    # Apply solution and re-shuffle with departure cut-off time
    prioritised_and_filtered_passengers = prioritisation_function(
        passengers, cut_off_time)

    # Sum totalNumberOfRequests across all passengers
    for i in range(len(passengers)):
        totalNumberOfRequests += passengers[i].getNumberOfRequests()
    #print("totalNumberOfRequests: " + str(totalNumberOfRequests))

    # Print sequence of sorted departure times
    #print("Sequence of prioritised departure times:")
    prioritised_filtered_list = []
    for i in range(len(prioritised_and_filtered_passengers)):
        #print(prioritised_and_filtered_passengers[i].departureTime, end=" ")
        prioritised_filtered_list.append(
            prioritised_and_filtered_passengers[i].departureTime)

    #print("\n")
    return {
        "total_number_of_requests": totalNumberOfRequests,
        "prioritised_filtered_list": prioritised_filtered_list
    }


def prioritisation_function(passengers, cutOffTime):

    passengers.sort(key=lambda x: x.askTimeToDeparture())
    
    idx = -1
    while True:
        if passengers[idx].askTimeToDeparture() > cutOffTime:
            passengers.pop()
        else:
            break

    return passengers


if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        #print("Usage: python my_script.py <JSON data>")
        sys.exit(1)

    # Parse the JSON data from the command line argument
    json_data = sys.argv[1]

    try:
        res = []
        data = json.loads(json_data)
        
        for test_case in data:
            output = execute(prioritisation_function,
                               test_case, test_case["cutOffTime"])
            
            res.append({
                "id": test_case["id"],  # test-id-123
                # [46, 75]
                "sortedDepartureTimes": output["prioritised_filtered_list"],
                "numberOfRequests": output["total_number_of_requests"],  # 4
            })
        print(res)  # Print the result to stdout
    except Exception as e:
        #print(f"Error: {str(e)}")
        sys.exit(1)
