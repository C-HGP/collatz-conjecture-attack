# Collatz Conjecture Attacker
This Python script provides a simple interactive console for exploring the Collatz Conjecture, also known as the 3n+1 problem.

## Features
- Bruteforce mode: The program starts at 1 and calculates the Collatz sequence for each successive integer. This process continues indefinitely until the program is manually stopped.
- Single Integer Mode: Users can input a specific integer to calculate its Collatz sequence. The program will display each step and the total count of steps needed to reach 1.

## Usage
To use this script, run it in a Python 3 environment. The console will guide you through the available options.

## Caution
The Bruteforce mode can potentially consume significant system resources due to its indefinite nature. Use this option with caution.

## About the Collatz Conjecture
The Collatz Conjecture is an unsolved mathematical conjecture that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.
