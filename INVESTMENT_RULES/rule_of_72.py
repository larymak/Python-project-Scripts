# Get Aannual fixed interest rate
fixed_interest_rate = input("Please enter the Annual Fixed interest rate (don't use % sign): ")


def calculate_time_taken_to_double(fixed_interest_rate):
    # A simple formula calulate the time it takes to double an investment.
    time_taken = 72/float(fixed_interest_rate)
    return time_taken

time_taken_to_double = round(calculate_time_taken_to_double(fixed_interest_rate),2)
print(f"Your investment will take {time_taken_to_double} year(s) to double!")