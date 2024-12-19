import math

def remaining_gifts(gifts, k):
    for _ in range(k):
        # Find the index of the pile with the maximum number of gifts
        max_index = gifts.index(max(gifts))
        # Calculate the number of gifts to leave behind
        gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))
    
    # Sum up the remaining elements in the list
    return sum(gifts)

# Example usage
gifts = [25, 64, 9, 4, 100]
k = 4
print(remaining_gifts(gifts, k))  # Output: 29

gifts = [1, 1, 1, 1]
k = 4
print(remaining_gifts(gifts, k))  # Output: 4