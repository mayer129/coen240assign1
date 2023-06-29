# Travis Mayer, COEN 240
import math

dataPointTuple = ((2,2), (4,6), (5,4), (7,8), (8,10), (10,12))


length = len(dataPointTuple)
x_bar = int((1/length) * sum(i for i, j in dataPointTuple))
y_bar = int((1/length) * sum(j for i, j in dataPointTuple))

s_x_sq = int((1/length) * sum((i-x_bar)**2 for i, j in dataPointTuple))
s_y_sq = (1/length) * sum((j-y_bar)**2 for i,j in dataPointTuple)
s_xy = (1/length) * sum((i-x_bar)*(j-y_bar) for i, j in dataPointTuple)
r = s_xy/math.sqrt((s_x_sq * s_y_sq))
r_sq = r**2
e = length * s_y_sq * (1 - r_sq)
b = s_xy/s_x_sq
a = y_bar - (b * x_bar)

print("x_bar:", x_bar)
print("y_bar:", y_bar)
print("s_x_sq:", s_x_sq)
print("s_y_sq:", str(round(s_y_sq, 4)))
print("s_xy:", str(round(s_xy, 4)))
print("r:", str(round(r, 4)))
print("r_sq:", str(round(r_sq, 4)))
print("E:", str(round(e, 4)))
print("b:", str(round(b, 4)))
print("a:", str(round(a, 5)))

print("Equation of Regression Line: y =", str(round(a, 5)), f"+ {str(round(b, 4))}𝑥\n")

y_hat_vals = []
e_vals = []
for i , j in dataPointTuple:
    temp = a + b * i
    y_hat_vals.append(temp)
    e_vals.append(-1 * (temp - j))

for index, val in enumerate(y_hat_vals):
    print(f"y_hat_{index+1}:", val)
print()
for index, val in enumerate(e_vals):
    print(f"e_{index+1}:", val)
