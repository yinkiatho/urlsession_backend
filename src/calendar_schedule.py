import json
from typing import Dict, List
import re
import sys

test = [{
    "lessonRequestId": "LR1",
    "duration": 1,
    "potentialEarnings": 100,
    "availableDays": ["monday", "wednesday"]
}, {
    "lessonRequestId": "LR2",
    "duration": 2,
    "potentialEarnings": 50,
    "availableDays": ["monday"]
}, {
    "lessonRequestId": "LR3",
    "duration": 12,
    "potentialEarnings": 1000,
    "availableDays": ["wednesday"]
}, {
    "lessonRequestId": "LR4",
    "duration": 13,
    "potentialEarnings": 10000,
    "availableDays": ["friday"]
}]


def generate(requests):
    max_duration = 12
    
    #reorder requests by potential earnings
    requests = list(filter(lambda x: x["duration"] <= max_duration, sorted(requests, key=lambda x: x["potentialEarnings"], reverse=True)))
    
    #create a dictionary of available days, input as tuple of (lessonid, time, potential earnings)
    available_days = {
        'monday': [],
        'tuesday': [],
        'wednesday': [],
        'thursday': [],
        'friday': [],
        'saturday': [],
        'sunday': []
    }
    for request in requests:
        for day in request["availableDays"]:
            
            
            if request["duration"] <= max_duration or sum([x[1] for x in available_days[day]]) + request["duration"] <= max_duration:
                
                available_days[day].append((request["lessonRequestId"], request["duration"], request["potentialEarnings"]))
                available_days[day].sort(key=lambda x: x[2])
            
            elif sum([x[1] for x in available_days[day]]) + request["duration"] > max_duration:
                #iterate through lessons in the day, if duration of lesson is less than current lesson, replace
                for i in range(len(available_days[day])):
                    if available_days[day][i][1] <= request["duration"] and available_days[day][i][2] < request["potentialEarnings"]:
                        available_days[day][i] = (request["lessonRequestId"], request["duration"], request["potentialEarnings"])
                        available_days[day].sort(key=lambda x: x[2])
                    break
            else:
                continue
    
    #filter out only days with lessons, keeping only keyid in the list
    available_days = {k: [x[0] for x in v] for k, v in available_days.items() if v}
    return json.dumps(available_days)
#print(generate(test))


if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: python my_script.py <JSON data>")
        sys.exit(1)

    # Parse the JSON data from the command line argument
    json_data = sys.argv[1]
    # print(json_data)
    try:
        data = json.loads(json_data)
        result = generate(data)
        print(result)  # Print the result to stdout
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
