
# Debt Repayment Simulation

A Python project exploring debt repayment scenarios through financial
modeling, Monte Carlo simulation, and sensitivity analysis.

## Project Overview

This project demonstrates how simple computational models can help
compare hypothetical financial scenarios over a five-year horizon.

All data used in this public portfolio project are synthetic and
illustrative. The project does not contain real client information.

## Objectives

- Compare different monthly savings strategies.
- Simulate 1,000 hypothetical financial outcomes.
- Evaluate how savings levels affect the final net balance.
- Demonstrate reproducible analysis using Python.

## Methodology

### 1. Scenario Analysis

Compares four hypothetical monthly savings strategies:

- Conservative
- Moderate
- Target
- Aggressive

### 2. Monte Carlo Simulation

Generates 1,000 simulations using randomly selected monthly savings
between 0 and 250 monetary units.

A fixed random seed makes the results reproducible.

### 3. Sensitivity Analysis

Evaluates the effect of different fixed monthly savings amounts
on the final net balance.

## Technologies

- Python
- `random`
- `statistics`

No external Python packages are required.

## Getting Started

### Requirements

- Python 3.10 or newer

### Run the project

Clone or download this repository, open a terminal in the project
directory, and run:

```bash
python simulation.py
```

The program prints the scenario comparison, Monte Carlo results,
and sensitivity analysis to the terminal.

## Model Assumptions and Limitations

- The initial debt is synthetic.
- The projection horizon is five years.
- Monthly savings are assumed to remain constant within each
  fixed scenario.
- Monte Carlo savings are sampled uniformly between 0 and 250.
- Interest, inflation, fees, and income changes are not modeled.
- The simulation is educational and does not predict an individual's
  actual financial future.

Results depend on the assumptions and simplifications used.

## Project Structure

```text
debt-simulation/
├── simulation.py
└── README.md
```

## Responsible Use

This project is for educational and portfolio demonstration
purposes only. It is not financial advice.

## Author

Data Science Portfolio Project
