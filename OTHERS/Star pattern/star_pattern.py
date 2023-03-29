# Pattern 1
# *
# **
# ***
# ****
# *****

# Loop through the rows from 0 to 5 (6 rows in total)
for i in range(6):
    # Loop through the columns from 0 to i (inclusive) for each row
    for k in range(i+1):
        # Print a star with no newline character
        print("*", end="")
    # Move to the next line
    print()

# Pattern 2
# *****
# ****
# ***
# **
# *

# Loop through the rows from 5 to 1 (inclusive)
for i in range(5, 0, -1):
    # Loop through the columns from 0 to i (inclusive) for each row
    for k in range(i):
        # Print a star with no newline character
        print("*", end="")
    # Move to the next line
    print()

# Pattern 3
#     *
#    **
#   ***
#  ****
# *****

# Loop through the rows from 0 to 4 (5 rows in total)
for i in range(5):
    # Loop through the columns from 1 to 5 for each row
    for j in range(1, 6):
        # Print a space with no newline character if j is less than or equal to 5-i
        if j <= 5-i:
            print(" ", end="")
        else:
            # Otherwise, print a star with no newline character
            print("*", end="")
    # Move to the next line
    print()

# Pattern 4
# *****
#  ****
#   ***
#    **
#     *

# Loop through the rows from 5 to 1 (inclusive)
for i in range(5, 0, -1):
    # Loop through the columns from 1 to 5 for each row
    for j in range(1, 6):
        # Print a space with no newline character if j is less than or equal to 5-i
        if j <= 5-i:
            print(" ", end="")
        else:
            # Otherwise, print a star with no newline character
            print("*", end="")
    # Move to the next line
    print()

# Pattern 5
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

# Loop through the rows from 0 to 8 (9 rows in total)
for i in range(9):
    # Determine the number of spaces and stars to print for this row
    if i <= 4:
        spaces = 4 - i
        stars = 2*i + 1
    else:
        spaces = i - 4
        stars = 17 - 2*i
    # Loop through the columns for each row
    for j in range(1, 11):
        # Print spaces or stars as appropriate for the current column
        if j <= spaces:
            print(" ", end="")
        elif j <= spaces + stars:
            print("*", end="")
    # Move to the next line
    print()
