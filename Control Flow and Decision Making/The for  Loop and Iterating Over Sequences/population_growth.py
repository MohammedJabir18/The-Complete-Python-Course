"""
Problem
--------
The current population of town is 10000. The population of town is increasing at the rate of 10% per year. You have to
write a program to find out the population at the end of each of the last 10 years.
"""

current_population = 10000
increasing_rate = 10 / 100
finding_years = 10

for i in range(finding_years, 0, -1):
    print(f"{i} year population is {round(current_population, 2)}")
    current_population = current_population / (1+increasing_rate)
