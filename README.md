## CS2-Aviles-LucasSebastian

## Description
This program calculates the total cost of your electricity bill

## Version 1 - Original code without input validation
# Input:
- Accepts a customer's name, previous electricity reading, and current reading
# Process:
- Subtracts the previous reading from the current reading and multiplies it by the rate (P12.90 per kilowatt), then displays the product (total bill) rounded to two decimal points.
# Output: 
- Total bill
# Input Validation: 
- none  

## Version 2 - Updated code with validation rules
# Input:
- Asks for a customer's name, rejecting blank entries.
- Asks for previous meter reading, rejecting numbers lower than zero.
- Asks for current meter reading, rejecting inputs lower than previous input
# Process:
- Subtracts the previous reading from the current reading and multiplies it by the rate (P12.90 per kilowatt), then displays the product (total bill) rounded to two decimal points.
# Output: 
- Total bill
# Input Validation: 
1. Customer name -- must not be empty
2. Previous reading -- must be at least zero
3. Current reading -- must be greater than or equal to previous reading
