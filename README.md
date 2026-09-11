# DevOps Learning Log

This repository documents my progress as I learn the skills needed for cloud infrastructure and DevOps interships.

## Current Focus 

- Python fundamentals
- Terminal commands 
- Git and  GitHub

## Day 1 

I created and ran a Python program that calculates how many minutes remain in my daily goal.

## Day 2 - Weekly DevOps Study Planner

I made a Python program that calculates weekly study time and checks whether the user reached a 600-minute weekly goal.

### Skills Practiced

- Collecting user input with `input()`
- Converting input into integers with `int()`
- Storing calculated values in variables
- Using multiplication
- Making decisions with `if` and `else`
- Comparing numbers with `>=`
- Testing true and false branches

### Test Results

- 90 minutes for 5 days produced 450 minutes and reported that 150 more minutes were needed.
- 120 minutes for 5 days produced 600 minutes and reported that the weekly goal was reached.

## DevOps Disk Usage Checker

This Python program asks the user for the current disk usage percentage. If the entered usage is greater than or equal to the warning threshold of 80%, it displays a warning or it reports that disk usage is healthy.

## Skills Used

- Collecting user input with `input()`
- Converting input into a whole number with `int()`
- Storing values in variables
- Making decisions with `if` and `else`
- Comparing values with the `>=` operator
- Using a condition that evaluates to `True` or `False`

## Test cases

- Below threshold: Input `79%` → Output: `Disk usage is healthy.`
- Equal to threshold: Input `80%` → Output: `Warning disk usage is high.`
- Above threshold: Input `95%` → Output: `Warning disk usage is high.`

## Filename

- [`disk_usage_checker.py`](disk_usage_checker.py)

## Day 3 - CPU Temperature Checker

This command-line Python program asks the user to enter a CPU temperature in degrees Celsius it uses ordered conditions to classify the entered value as safe, warning, or critical.

This learning project evaluates a user-provided temperature; it does not read live CPU sensor data.

### Classification Rules

* Below 85°C: Safe
* From 85°C through 94°C: Warning
* 95°C or higher: Critical

### Skills Practiced

* Collecting user input with `input()`
* Converting input into a whole number with `int()`
* Storing values in variables
* Comparing numbers with `>=`
* Creating three branches with `if`, `elif`, and `else`
* Ordering conditions from the highest threshold to the lowest
* Testing boundary values

### Test Results

| Input | Branch | Result   |
| ----: | ------ | -------- |
|  84°C | `else` | Safe     |
|  85°C | `elif` | Warning  |
|  94°C | `elif` | Warning  |
|  95°C | `if`   | Critical |
| 100°C | `if`   | Critical |

All five test cases produced the expected results.

### Run the Program

```bash
python3 cpu_temperature_checker.py
```

### Project File

* [`cpu_temperature_checker.py`](cpu)

