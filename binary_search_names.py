
# original code:
def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list? 
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False



# updated code with sorted list
# The binary search algorithm assumes a sorted list to work correctly

def find_item(lst, item):
    # Sort the list
    sorted_lst = sorted(lst) #sorted the list

    # Returns True if the item is in the list, False if not.
    if len(sorted_lst) == 0:
        return False

    # Is the item in the center of the list?
    middle = len(sorted_lst) // 2
    if sorted_lst[middle] == item:
        return True

    # Is the item in the first half of the list?
    if item < sorted_lst[middle]:
        # Call the function with the first half of the list
        return find_item(sorted_lst[:middle], item)
    else:
        # Call the function with the second half of the list
        return find_item(sorted_lst[middle+1:], item)

    return False
  
#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
