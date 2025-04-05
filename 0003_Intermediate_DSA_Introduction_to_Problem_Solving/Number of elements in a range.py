"""
how many elements are there between [135, 246] (inclusive of them) ?
"""

def count_elements_in_range(start, end):
    return end - start + 1

# Example usage
start = 135
end = 246
print(f"Number of elements between {start} and {end} (inclusive): {count_elements_in_range(start, end)}")