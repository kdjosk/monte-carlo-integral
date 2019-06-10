import webbrowser
import random

def callWolfram(coefs, a, b):
    # compose the url string
    res = "https://www.wolframalpha.com/input/?i="
    for i in range(len(coefs)):
        res = res + str(coefs[i]) + "x^" + str(i) + "+%2B+"
    res = res[0:len(res)-4] + "dx+from+" + str(a) + "+to+" + str(b)

    #open in the browser
    webbrowser.open(res)

def getPolyVal(coefs, x):
    res = 0;
    for i in range(len(coefs)):
        res += coefs[i] * (x ** i)
    return res

def monteCarlo(coefs, a, b, n_steps, iterations):
    # get max and min values
    step = (b - a)/n_steps
    max_val = int(-1e9)
    min_val = -1 * max_val
    x = a

    while x < b:
        y = getPolyVal(coefs, x)
        max_val = max(max_val, y)
        min_val = min(min_val, y)
        x += step

    height = abs(max_val - min_val)
    width = abs(b - a)
    hits_neg = 0;
    hits_pos = 0;

    for i in range(iterations + 1):
        xr = random.random() * width + a
        yr = random.random() * height + min_val

        y = getPolyVal(coefs, xr)

        if y < 0:
            if yr > y and yr < 0:
                hits_neg += 1
        if y > 0:
            if yr < y and yr > 0:
                hits_pos += 1

    area_pos = width * height * hits_pos/iterations
    area_neg = width * height * hits_neg/iterations

    if min_val > 0:
        area_pos += min_val * width
    elif max_val < 0:
        area_neg += max_val * width

    return area_pos - area_neg



coefs = []
order = int(input("polynomial order: "))
a, b = [float(x) for x in input("limits: ").split()]

for i in range(order + 1):
    coefs.append(int( input("x^" + str(i) + ": ") ))

print(monteCarlo(coefs, a, b, 1000, 1000000))
callWolfram(coefs, a, b)
