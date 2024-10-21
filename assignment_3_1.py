"""
-----------------------------------------------------------------------
Problem 3.1: Quantities of chicken nuggets that fit within available order quantities
October 20, 2024 
Nishigandha Wankhade 
-----------------------------------------------------------------------
"""

def three_variable_diophantine(n):
    """
    Function to solve the Diophantine equation 6a + 9b + 22c = n.
    Input: n = number of chicken nuggets ordered by the customer
    Output: returns (solutions) possible number of combinations to buy nuggets
    """
    solutions = []

    # Try different values of c
    for c in range(0, n // 22 + 1):    # c cannot be greater than n // 22
        remaining = n - 22 * c   # solving for 6a + 9b = remaining

        # Check if remaining is divisible by 3 (since 6 and 9 are both divisible by 3)
        if remaining % 3 != 0:
            continue  # Skip this c if the remaining value isn't divisible by 3

        # Try different values of a and calculate b
        for a in range(0, remaining // 6 + 1):
            if (remaining - 6 * a) % 9 == 0:
                b = (remaining - 6 * a) // 9   # Calculate b
                solutions.append((a, b, c))    # Store the solution (a, b, c)

    return solutions



"""
Main Function
Input: Number of nuggets entered by the user
Output: Possible combinations for the entered quantity
"""
ans = 'y'
while ans.lower() == 'y':  # Continue until the user decides to stop
    try:
        n = int(input("\n\t\t How many chicken nuggets would you like to order? \t"))
        solutions = three_variable_diophantine(n)

        if solutions:
            print(f"\n\t\tFor an order size of {n}, choose from the following {len(solutions)} option(s):")
            for i, sol in enumerate(solutions):        # To print all possible combinations
                print(f"\n\t\tOption {i + 1}: 'Six_piece': {sol[0]}, 'Nine_piece': {sol[1]}, 'Twenty_two_piece': {sol[2]}")
        else:
            print("\n\n\t\tSORRY...!...You cannot order the requested quantity :( ")
                    
        ans = input("\n\n\t\tDo you want to reorder [y/n]? ")
        if ans.lower() != 'y':
                print("\n\t\tThank you! Have a nice day!")
                break
        
    except ValueError:           # To check wheather entered data is a valid number or not
        print("\n\t\t Please enter a valid number.")
