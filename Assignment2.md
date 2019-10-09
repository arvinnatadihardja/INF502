# Assignment 2: Python Basics

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Sept-19th 11:59PM
* **How to submit**: For each item, provide an answer as requested in the item (usually the source code + explanations + iteractive shell output)
  - In your GitHub repository called *INF502* (same used for the Assignment 1) create a file called *"Assignment2.md"* with your answers (I will allow the answer in PDF format for those who prefer, but I strongly encourage using Markdown.)
  Remember to invite me to see your new repository (if you did not for Assignment 1).
  - I will evaluate the latest commit before 11:59PM (Sept-19th)

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.


```
from math import sqrt
def pythagoreanTheorem(length_a, length_b):

print("Lengths of shorter triangle sides?:")
def pythagoreanTheorem (length_a, length_b)
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a ** 2 + b ** 2)
print(" hypotenuse =", c)

```
Present your source code and the output of three example runs.

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.



```
my_list = [1, 2, 3, 4]


def list_mangler(list_in):
    for i in range(len(my_list)):
        if i % 2 == 0:
            return i * i
    else:
        return i * i * i

    print list_mangler

```

Present a short (no more than a couple of sentences) description of your solution approach. Show your source code and the output of three example runs.

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for to_drop equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.


```
_list = []


def calc_average(total):
    return total / 5


def determine_grade(grade):
    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 80 and grade <= 89:
        return 'B'
    elif grade >= 70 and grade <= 79:
        return 'C'
    elif grade >= 60 and grade <= 69:
        return 'D'
    else:
        return 'F'


while True:
    grade = int(input('Enter grade: '))
    _list.append(grade)

    avg = calc_average(sum(_list))
    abc_grade = ' '.join([determine_grade(mark) for mark in _list])

    if len(_list) > 5:
        break

print('Average grade is: ', avg)
print('Letter grades for entered grades are: ', abc_grade)
```

Present a short (no more than a couple of sentences) description of your solution approach. Then show your source code and the  output of three example runs.

**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

For example:
```
>>> odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
>>> odd_even_filter([3, 9, 43, 7])
[[], [3, 9, 43, 7]]
>>> odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```
Present a short (no more than a couple of sentences) description of your solution approach. Then show your source code and the interactive shell output of three example runs.
