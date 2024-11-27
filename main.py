    
def can_nest(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

def longest_box_sequence(boxes):
    # Sort the boxes first by length, then by breadth, then by height
    boxes.sort(key=lambda x: (x[0], x[1], x[2]))

    # Apply LIS on the sorted boxes based on breadth and height
    n = len(boxes)
    dp = [1] * n  # dp[i] will store the length of the longest increasing subsequence ending at index i

    for i in range(1, n):
        for j in range(i):
            if can_nest(boxes[j], boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage
boxes = [(1, 5, 6), (3, 4, 5), (1, 2, 3), (6, 2, 8), (5, 5, 1), (2, 3, 1)]
result = longest_box_sequence(boxes)
print(f"The largest number of boxes that can be packed in sequence is: {result}")
	