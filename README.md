# Django Signals Assignment

## Project Overview

This project demonstrates the behavior of Django Signals with respect to:

1. Synchronous execution
2. Thread execution
3. Database transactions

It also contains the implementation of an iterable Rectangle class.

## Technologies Used

* Python
* Django
* SQLite

## Endpoints

### Signal Test

http://127.0.0.1:8000/signal-test/

Demonstrates:

* Signal execution
* Thread identification
* Synchronous behavior

### Transaction Test

http://127.0.0.1:8000/transaction-test/

Demonstrates:

* Transaction rollback
* Signal participation in transactions

## Results

### Question 1

Django Signals are synchronous by default.

### Question 2

Django Signals execute in the same thread as the caller.

### Question 3

Django Signals execute within the same database transaction as the caller.

## Author

Sanya Jain
