# 0 x02-minimum_operations

## Description

In a text file, there is a single character H. Your text editor can execute only two
operations in this file: Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result in exactly n H characters
in the file.

## Some Rules

1. Never do 2 copy operations simultaneously (useless additional operation)
2. All numbers from 2 upward have atleast one solutoin (Copy once and paste n-times depending on the number)
3. All prime numbers follos the previous rule (Since it is not possible to break this number as the product of smaller number of operation)

## Procedure

To acomplish this task, we divided the work load into specialized operations

1. Fragment Number: In this opeartion, we consider breaking the given number n into 2 different numbers (factors)
   which are closer to each other in order to reduce the possible representation of one of the numbers in the other.

```bash
    4   =>  [1, 4]  | [2, 2]                        // Selected is [2, 2]
    12  =>  [1, 12] | [2, 6]  | [3, 4]              // Selected is [3, 4]
    40  =>  [1, 40] | [2, 20] | [4, 10] | [5, 8]    // Selected is [5, 8]
```

This is to make sure that an element is as less represented in the other as possible.

2. Process a pair: Processing a node consist of getting the number of operations required to return the lowest number
   of operations for each child. We should note that a node is made up of a pair of 2 numbers (the closest factors of thier parent node).
   We use a rucursion to put in place this function.

In general, if a node contains 1 as a child, the other is returned as the number of operations.

```bash
    process([x, 1]) or process([1, x]) => x
    // This is because one is considered as the unique copy of the character in the file.
    // So to copy it x-times, we need to have exactly x-operations to do that.
    // i.e copy_all() once and paste() (x-1)-times
```

And if there are different numbers in the node, the we recursively execute the processing on the
left and right elements of the node.

```bash
    process([x, y]) => process(fragment(x)) + process(fragment(y))
```

3. The monitoring function: This function is in charge of putting in place the basic initialization operations and test.
   These ones are:

- If n is 1 or 0 or less, then no operation is needed, so it returns 0.
- For other values, return the number of operations for the given node

## Some returned values

```bash
    Min # of operations to reach 4 char:         4
    Min # of operations to reach 12 char:        7
    Min # of operations to reach 16 char:        8
    Min # of operations to reach 1000 char:     21
    Min # of operations to reach 10000 char:    28
    Min # of operations to reach 20000 char:    30
    Min # of operations to reach 30000 char:    31
```
