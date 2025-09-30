def fun_avg(x, y):
    return (x + y) * 0.5

def milnes_method(f, x0, x1, x2, x3, y0, y1, y2, y3, x4):
    x = [x0, x1, x2, x3, x4]
    y = [y0, y1, y2, y3, None]
    h = x[1] - x[0]

    y1_value = f(x[1], y[1])
    y2_value = f(x[2], y[2])
    y3_value = f(x[3], y[3])

    y[4] = y[0] + (4 * h / 3) * (2 * y3_value - y2_value + 2 * y1_value)
    y4_value = f(x[4], y[4])

    return y[2] + (h / 3) * (y2_value + 4 * y3_value + y4_value)

print(milnes_method(fun_avg, 0, 0.5, 1.0, 1.5, 2, 2.636, 3.595, 4.968, 2))
