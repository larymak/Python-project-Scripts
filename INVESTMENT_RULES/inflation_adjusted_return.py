Inflation_Adjsted_Return_Summary = """
Learn More about this investment rule in README.md located in INVESTMENT_RULES folder** 
 """

print(Inflation_Adjsted_Return_Summary)

# Get the Avg Investment Rate of Return and Avg Inflation Rate
invest_rate_return = float(input("What is expected average  Rate of Return (don't use % sign): "))/100
avg_inflration_rate = float(input("What is your avg inflation rate?: "))/100


def inflation_adjusted_return(invest_rate_return, avg_inflration_rate):
    # Simple formula is : ((1 + Investment return percentage) / (1 + Inflation rate percentage) - 1) x 100
    inflration_adjusted_return_val = (((1 +invest_rate_return )/(1 +avg_inflration_rate)) - 1) * 100
    return inflration_adjusted_return_val

real_return = round(inflation_adjusted_return(invest_rate_return, avg_inflration_rate),2)
print(f"Your Actual Rate of Return adjusted to the inflation is {real_return}%. Not {invest_rate_return*100}% ")