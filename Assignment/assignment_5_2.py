"""
Assignment 5 Problem 1: Variable Retirement Investment
August 6, 2025
Johnpaul Nnaji
"""

def variableInvestor(salary, p_rate, v_rates):
    """
    Simulates a retirement account where the investment grows at different rates each year.

    :param salary: Annual salary (float)
    :param p_rate: Employee contribution rate (decimal, e.g., 0.05 for 5%)
    :param v_rates: List of annual growth rates (list of floats)
    :return: List of account values at the end of each year, after applying growth and contributions.
    """
    account_values = []
    balance = 0

    # Employer base contribution: 5%, match up to 5% of employee contribution
    match_rate = min(p_rate, 0.05)
    annual_contribution = salary * (p_rate + 0.05 + match_rate)

    for i, g_rate in enumerate(v_rates):
        if i > 0:
            # Apply growth only from year 2 onward
            balance *= (1 + g_rate)
        # Add this year's contribution
        balance += annual_contribution
        account_values.append(round(balance, 2))

    return account_values


# ----------------------------
# Testing (comment out before submission)
# ----------------------------
# salary = 50000
# p_rate = 0.05
# v_rates = [0.09, 0.07, 0.05]  # growth rates for 3 years
# Expected: [7500.0, 15525.0, 23801.25]
# print("Account values:", variableInvestor(salary, p_rate, v_rates))
