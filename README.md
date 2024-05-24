# ImapactAnalysis assessment

## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.


Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773

## How to run the code

pre-requisites: ```python3``` <br />
command: ```python3 attendance.py```

## Approach

* Number of possible attendance combinations : 2 => i.e., student can **attend** or be **abscent** <br />
  total_possible combinations = 2^(n) where n is number of days
* Filter those combinations which has consecutive **4 absents**.
* Further to find the chance of missing the graduation, **taking note of the point mentioned in the question,
  The graduation will be on the last day of the academic year**, filter out those attendance series which has abscent marked at the last of each.
