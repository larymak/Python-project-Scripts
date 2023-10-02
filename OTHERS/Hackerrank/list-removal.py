list_a = ["car", "place", "tree", "under", "grass", "price"] 

remove_items_containing_a_or_A = lambda list_1 : [item for item in list_1 if "a" not in item.lower()]

print(remove_items_containing_a_or_A(list_a))
