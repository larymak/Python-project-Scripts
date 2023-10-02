t_1 = (1,4,9,16,25,36)

t_modified = tuple(i**2 for i in t_1)

print("t_modified:",t_modified)

print("Element at index postion 4 of t_modified:",t_modified[4])

t_sliced = t_modified[1:4]
print("t_sliced:",t_sliced)