Week 3 Assignment: Name Splitter, Bug Hunt & First Decisions
This repository contains my Week 3 Python assignment.

name_greeter.py — Splits a user's full name and greets them using their first name.
bug_hunt.py — Fixes three bugs and demonstrates debugging using error messages.
ticket_checker.py — Checks whether a user is an adult and displays the appropriate ticket price.
screenshots/ — Contains screenshots of the programs running.
The bug that took the longest to find was the problem with adding 1 to the age because input() returns a string. The error message helped me understand that Python could not add an integer to a string, so I converted the age to an integer before adding 1.
