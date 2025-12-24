"""
Program to find the most repetitive element in a list
"""

# Method 1: Using dictionary (manual counting)
def find_most_repetitive_dict(lst):
    """
    Find the most repetitive element using dictionary
    
    Args:
        lst (list): Input list
    
    Returns:
        tuple: (most_common_element, count)
    """
    if not lst:
        return None, 0
    
    # Count occurrences
    count_dict = {}
    for element in lst:
        count_dict[element] = count_dict.get(element, 0) + 1
    
    # Find maximum
    max_element = max(count_dict, key=count_dict.get)
    max_count = count_dict[max_element]
    
    return max_element, max_count


# Method 2: Using Counter from collections module
def find_most_repetitive_counter(lst):
    """
    Find the most repetitive element using Counter
    
    Args:
        lst (list): Input list
    
    Returns:
        tuple: (most_common_element, count)
    """
    from collections import Counter
    
    if not lst:
        return None, 0
    
    counter = Counter(lst)
    most_common = counter.most_common(1)[0]
    
    return most_common[0], most_common[1]


# Method 3: Using max with count (simple but less efficient)
def find_most_repetitive_simple(lst):
    """
    Find the most repetitive element using count method
    
    Args:
        lst (list): Input list
    
    Returns:
        tuple: (most_common_element, count)
    """
    if not lst:
        return None, 0
    
    # Find unique elements
    unique_elements = set(lst)
    
    # Find element with maximum count
    max_element = max(unique_elements, key=lst.count)
    max_count = lst.count(max_element)
    
    return max_element, max_count


# Example usage
if __name__ == "__main__":
    # Given list
    L1 = [1, 2, 2, 3, 2, 3, 4, 5]
    
    print("Original List:", L1)
    print("="*50)
    
    
    element1, count1 = find_most_repetitive_counter(L1)
    print("\nMethod 2 (Counter):")
    print(f"Most repetitive element: {element1}")
    print(f"Number of occurrences: {count1}")
    
        
    # Additional: Show all elements with their counts
    print("\n" + "="*50)
    print("All elements with their counts:")
    from collections import Counter
    counter = Counter(L1)
    for element, count in counter.most_common():
        print(f"Element {element}: appears {count} time(s)")
    
    # Test with other examples
    print("\n" + "="*50)
    print("Testing with other lists:")
    
    test_lists = [
        [5, 5, 5, 1, 2, 3],
        ['a', 'b', 'a', 'c', 'a', 'b'],
        [10, 20, 30, 10, 10, 20]
    ]
    
    for i, test_list in enumerate(test_lists, 1):
        element, count = find_most_repetitive_counter(test_list)
        print(f"\nTest {i}: {test_list}")
        print(f"Most repetitive: {element} (appears {count} times)")