def max_fruit_value(w, v, f):
    n = len(f)
    dp = [[0] * (v + 1) for _ in range(w + 1)]

    for i in range(n):
        weight, volume, value = f[i]
        for weight_limit in range(w, -1, -1):
            for volume_limit in range(v, -1, -1):
                if weight_limit >= weight and volume_limit >= volume:
                    dp[weight_limit][volume_limit] = max(
                        dp[weight_limit][volume_limit],
                        dp[weight_limit - weight][volume_limit - volume] + value
                    )

    return dp[w][v]


# Test cases
input1 = {"w": 100, "v": 150, "f": [[60, 70, 60], [30, 80, 40], [35, 70, 70]]}
input2 = {"w": 100, "v": 150, "f": [[110, 80, 60], [80, 155, 90]]}

output1 = max_fruit_value(input1["w"], input1["v"], input1["f"])
output2 = max_fruit_value(input2["w"], input2["v"], input2["f"])

print(output1)  # Output: 130
print(output2)  # Output: 0

