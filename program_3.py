#Timothy Foster, 2/24/25, Tax Rate Program

#Define the variables that will be used in the functions.
countyTax = 0
stateTax = 0
totalTax = 0

#Get user input for the total sales.
sales = float(input("Enter the amount of total sales in dollars for the month."))

#Create the function to calculate the county tax.
def get_county_tax ():

    #Calculate using the given formula.
    countyTax = sales * 0.025

    #Return the value.
    return countyTax

#Create the function to calculate the state tax.
def get_state_tax ():

    #Calculate using the given formula.
    stateTax = sales * 0.05

    #Return the value.
    return stateTax

#Create the function to calculate the total tax.
def get_total_tax ():

    #Calculate by adding the previous two values.
    totalTax = get_county_tax() + get_state_tax()

    #Return the value.
    return totalTax

#Print, recall, and round the values.
print(f"The amount of county sales tax in dollars was {get_county_tax(): .2f}.")
print(f"The amount of sales tax tax in dollars was {get_state_tax(): .2f}.")
print(f"The total amount of sales tax in dollars was {get_total_tax(): .2f}.")
