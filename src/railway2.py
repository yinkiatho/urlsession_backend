import json


def railway_combination(length, track_pieces):
    # Create a memoization table to store the results of previous calculations.
    memo = {}

    unique_combinations = set()  # Use a set to store unique combinations

    def count_combinations(remaining_length, combination):
        print(combination)
        if remaining_length < 0:
            return

        if remaining_length == 0:
            # Add a sorted tuple as a unique combination
            
            unique_combinations.add(tuple(sorted(combination)))
            print(unique_combinations)
            return

        # Check if the result is already memoized
        if remaining_length in memo:
            return

        for track_piece in track_pieces:
            count_combinations(remaining_length - track_piece,
                               combination + [track_piece])

        # Memoize the result for the current remaining_length
        memo[remaining_length] = 1

    # Initialize the memoization table with a base case
    memo[0] = 1

    # Call the recursive function
    count_combinations(length, [])

    # Convert unique_combinations back to a list and return its length
    return len(list(unique_combinations))


def evaluate_railway_combinations(json_input):
    inputs = json_input
    outputs = []

    for input in inputs:
        input = input.split(", ")
        length = int(input[0])
        num_track_pieces = int(input[1])
        track_pieces = [int(track_piece)
                        for track_piece in input[2:2 + num_track_pieces]]
        output = railway_combination(length, track_pieces)
        outputs.append(output)

    return json.dumps(outputs)


# Test your function with a sample input
test_input = ["5, 3, 2, 1, 4"]
result = evaluate_railway_combinations(test_input)
print(result)
