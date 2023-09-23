import json
from typing import Dict, List
import re
import sys
test = ["5", "3", "2", "1", "4"]

def railway_combination(length, track_pieces):
  
  # Create a memoization table to store the results of previous calculations.
  memo = {}
  combinations = set()
  def count_combinations(remaining_length, combination):
    #print(remaining_length, combination)

    if remaining_length < 0:
      return

    if remaining_length == 0:
      combinations.add(tuple(sorted(combination)))

    #if remaining_length in memo:
      #return memo[remaining_length]

    #count = 0
    for track_piece in track_pieces:
      count_combinations(remaining_length - track_piece, combination + [track_piece])

    #memo[remaining_length] = count
  count_combinations(length, [])
  return combinations  


def evaluate_railway_combinations(json_input):
  #print(json_input)
  inputs = json_input
  outputs = []
  #print(inputs)

  for input in inputs:
    input = input.split(", ")
    #print(input)
    length = int(input[0])
    num_track_pieces = int(input[1])
    track_pieces = [int(track_piece) for track_piece in input[2:2 + num_track_pieces]]
    output = railway_combination(length, track_pieces)
    #print(output)
    #unique = list([sorted(x) for x in output])
    #print(unique)
    outputs.append(len(output))
    
  #print(json.dumps(outputs))
  return json.dumps(outputs)


def count_railway_combinations(length, track_pieces):
    # Sort the track pieces to ensure equivalence of combinations
    track_pieces.sort()

    # Create a memoization dictionary to store results
    memo = {}

    def count_combinations(remaining_length, last_track_piece):
        if remaining_length == 0:
            return 1
        if (remaining_length, last_track_piece) in memo:
            return memo[(remaining_length, last_track_piece)]

        count = 0
        for track_piece in track_pieces:
            if track_piece >= last_track_piece and remaining_length >= track_piece:
                count += count_combinations(remaining_length -
                                            track_piece, track_piece)

        memo[(remaining_length, last_track_piece)] = count
        return count

    return count_combinations(length, 0)


def evaluate_railway_combinations2(json_input):
    inputs = json_input
    outputs = []

    for input_str in inputs:
        input_data = input_str.split(", ")
        length = int(input_data[0])
        num_track_pieces = int(input_data[1])
        track_pieces = [int(piece)
                        for piece in input_data[2:2 + num_track_pieces]]
        count = count_railway_combinations(length, track_pieces)
        outputs.append(count)

    return json.dumps(outputs)


#print(evaluate_railway_combinations2(
#    ["5, 3, 2, 1, 4", "3, 3, 4, 1, 2", "11, 1, 2"]))
if __name__ == '__main__':
    
  if len(sys.argv) != 2:
        print("Usage: python my_script.py <JSON data>")
        sys.exit(1)

    # Parse the JSON data from the command line argument
  json_input = sys.argv[1]
  #print(json_input)
  try:
      data = json.loads(json_input)
    #print(data)
      result = evaluate_railway_combinations2(data)
      print(result)  # Print the result to stdout
  except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
# Example usage with generic JSON data and statements
# print(json.dumps(result, indent=2))
