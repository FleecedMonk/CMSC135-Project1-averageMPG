### CMSC135 - Project 1 - Average MPG Calulator
### Purpose - To make a program that will calculate the average MPG
### Design Requirements: To use what we have learned in chapters 1 and 2
### regarding the input, output, and print functions

### Get the miles travelled and assign it to the miles_travelled
### variable
miles_travelled = float(input('Enter the miles travelled : '))

### Get the amount of gasoline used and assign it to the
### gasoline_used variable
gasoline_used = float(input('Enter the amount of gasoline used : '))

### calculate the the MPG and assigned it to the
### calculated_MPG variable
calculated_MPG = miles_travelled/gasoline_used

### Display the MPG
print('You used ', calculated_MPG, 'per gallon.')
