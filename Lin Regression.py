"""
 HOW LINEAR REGRESSION WORKS(ALGORITHM)???
 _________________________________________
 -----------------------------------------
 y = mx + b; where: m = slope of the line
                    b = y intercept
 If we have m and b we can predict the value of y for a given value of x.

 TO CALCULATE m :
 ----------------
    m = {( mean(x) * mean(y) ) - ( mean(x * y) ) } /
        {( mean(x) ** 2 ) - ( mean(x ** 2) )}

 TO CALCULATE b :
 ----------------
    b = {( mean(y) ) - ( m * mean(x) )}

 SQUARED ERROR:
 _______________________
 -----------------------
 Squared Error is the difference between (the y value of a data points for a
 particular value of x) and (the y value on regression line for same value of x)
 all to the power of 2

 To calculate the Coefficient of determination(r^2) :
    r^2 = 1 - [SE(y) / SE(mean(y))]; where: SE = squared error
                                            r^2 = Coefficient of determination
"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('ggplot')

# xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
# ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation == 'pos':
            val += step
        elif correlation == 'neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = ((mean(xs) * mean(ys)) - (mean(xs * ys))) / ((mean(xs) ** 2) - (mean(xs ** 2)))
    b = ((mean(ys)) - (m * mean(xs)))
    return m, b


def squared_error(ys_original, ys_line):
    return sum((ys_line - ys_original)**2)


def coefficient_of_determination(ys_original, ys_line):
    y_mean_line = [mean(ys_original) for y in ys_original]
    squared_error_reg = squared_error(ys_original, ys_line)
    squared_error_y_mean = squared_error(ys_original, y_mean_line)
    return 1 - (squared_error_reg / squared_error_y_mean)


xs, ys = create_dataset(40, 40, 3, 'neg')

m, b = best_fit_slope_and_intercept(xs, ys)
regression_line = (m * xs) + b

r_sqaured = coefficient_of_determination(ys, regression_line)
print(r_sqaured)

for_x = 8
predict_y = (m * for_x) + b

plt.scatter(xs, ys)
plt.scatter(for_x, predict_y, color='b', s=80)
plt.plot(xs, regression_line)
plt.show()
