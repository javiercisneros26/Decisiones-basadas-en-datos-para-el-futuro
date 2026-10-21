
"""
Debt Repayment Simulation
------------------------
Portfolio project demonstrating:
- Financial scenario analysis
- Monte Carlo simulation
- Sensitivity analysis

All values are synthetic and illustrative.
This model is educational, not financial advice.
"""

import random
from statistics import mean

# Synthetic example assumptions
INITIAL_DEBT = 5500.0
PROJECTION_YEARS = 5
MONTHS_PER_YEAR = 12
SIMULATIONS = 1000
RANDOM_SEED = 42

# Fixed monthly savings for each scenario
SCENARIOS = {
    "Conservative": 0,
    "Moderate": 75,
    "Target": 125,
    "Aggressive": 200,
}

# Savings levels used in sensitivity analysis
SENSITIVITY_LEVELS = [0, 50, 100, 150, 200, 250, 300]


def calculate_final_balance(monthly_savings):
    """Calculate net balance after the projection period."""
    total_savings = (
        monthly_savings
        * MONTHS_PER_YEAR
        * PROJECTION_YEARS
    )
    return INITIAL_DEBT - total_savings


def show_scenarios():
    """Compare fixed monthly savings scenarios."""
    print("\n=== SCENARIO ANALYSIS ===")

    for name, monthly_savings in SCENARIOS.items():
        final_balance = calculate_final_balance(monthly_savings)

        if final_balance > 0:
            status = "Debt remaining"
        else:
            status = "Debt covered"

        print(
            f"{name:12} | "
            f"Monthly savings: {monthly_savings:6.2f} | "
            f"Final net balance: {final_balance:8.2f} | "
            f"{status}"
        )


def run_monte_carlo():
    """Simulate different monthly savings levels."""
    print("\n=== MONTE CARLO SIMULATION ===")

    random.seed(RANDOM_SEED)
    final_balances = []

    for _ in range(SIMULATIONS):
        monthly_savings = random.uniform(0, 250)
        final_balance = calculate_final_balance(monthly_savings)
        final_balances.append(final_balance)

    debt_covered = sum(
        balance <= 0 for balance in final_balances
    )
    probability = debt_covered / SIMULATIONS * 100

    print(f"Simulations: {SIMULATIONS}")
    print(f"Debt covered in simulations: {debt_covered}")
    print(f"Share with debt covered: {probability:.1f}%")
    print(f"Average final net balance: {mean(final_balances):.2f}")
    print(f"Lowest final net balance: {min(final_balances):.2f}")
    print(f"Highest final net balance: {max(final_balances):.2f}")

    return final_balances


def show_sensitivity():
    """Measure how savings affect the final net balance."""
    print("\n=== SENSITIVITY ANALYSIS ===")
    print("Monthly savings | Final net balance")

    for monthly_savings in SENSITIVITY_LEVELS:
        final_balance = calculate_final_balance(monthly_savings)
        print(f"{monthly_savings:15.2f} | {final_balance:18.2f}")


def main():
    print("SYNTHETIC DEBT SIMULATION")
    print(f"Projection horizon: {PROJECTION_YEARS} years")
    print(f"Illustrative starting debt: {INITIAL_DEBT:.2f}")

    show_scenarios()
    run_monte_carlo()
    show_sensitivity()


if __name__ == "__main__":
    main()
