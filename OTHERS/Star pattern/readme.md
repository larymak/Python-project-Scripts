# Patterns in Python
This is a Python script that generates five different patterns using loops and print statements. The patterns are printed to the console.

## Pattern 1
The first pattern is a triangle of asterisks, with each row having one more asterisk than the previous row:

```
*
**
***
****
*****
```
The pattern is generated using a nested loop, with the outer loop iterating over the rows and the inner loop iterating over the columns in each row.

## Pattern 2
The second pattern is an upside-down triangle of asterisks, with each row having one less asterisk than the previous row:

```
*****
****
***
**
*
```

The pattern is generated using a nested loop similar to the first pattern, but with the rows iterating in reverse order.

## Pattern 3
The third pattern is a triangle of asterisks with leading spaces, with each row having one more asterisk than the previous row and one fewer space than the previous row:

```
    *
   **
  ***
 ****
*****
```
The pattern is generated using two nested loops, with the outer loop iterating over the rows and the inner loops iterating over the columns in each row. The number of spaces and asterisks printed in each row is determined based on the current row number.

## Pattern 4
The fourth pattern is an upside-down triangle of asterisks with leading spaces, with each row having one less asterisk than the previous row and one more space than the previous row:

```
*****
 ****
  ***
   **
    *
```
The pattern is generated using two nested loops similar to the third pattern, but with the rows iterating in reverse order.

## Pattern 5
The fifth pattern is a diamond made of asterisks and spaces, with the widest point of the diamond having nine asterisks and the narrowest point having one asterisk:

```
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
```
The pattern is generated using three nested loops, with the outer loop iterating over the rows and the inner loops iterating over the columns in each row. The number of spaces and asterisks printed in each row is determined based on the current row number.
