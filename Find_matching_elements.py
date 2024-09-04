# Using python without using set but should not be use time complexity of o(n*m), given 2 lists create a function that lets the user know whether these 2 lists have anything in common.
# For example:
# list1 = ['a','b','c']
# list2 = ['x','y',z']
# should return matching elements



def have_common_elements(list1, list2):
    # Create a dictionary to store elements from the first list
    element_dict = {}
    match_list = []
    
    # Add elements of the first list to the dictionary
    for element in list1:
        element_dict[element] = True
    
    # Check if any element of the second list is in the dictionary
    for element in list2:
        if element in element_dict:
            match_list.append(element)
    
    return match_list

# Example usage
list1 = ['a', 'b', 'c']
list2 = ['a', 'y', 'z','c']
print(have_common_elements(list1, list2))  # Output: False