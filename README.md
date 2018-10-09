# Convex-Hull
Incremental, Divide and Conquer and Jarvis code in Python language for solving classic Convex Hull geometrical problem

Firstly, you should know that the whole programs have 5 parameters, this will are described as following:
- *n = number of points you will create*
- *t = the distribution we will use, r if it is a rectangular distribution, e if it is an elliptic distribution*
- *a = if we are working over a rectangle this will represent the size, else, this will represent the diameter*
- *b = the height*
- *r = the rotation angle*

Here you will find 3 python files, the first is developed for the incremental solution for the Convex Hull, you should execute it in this way

```python incremental_hull.py n t a b r```

You should execute the second file in this way

```python dc_hull.py n t a b r```

And, finally, you should execute the third file like this.

```python jarvis_hull.py n t a b r```
