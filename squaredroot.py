import math
import turtle as trtl

# --- input number ---
x = input("enter a number: ") # try 25, 36, 49, etc.
x = int(x)


# --- compute square root as an integer grid size ---
n = int(math.isqrt(x))

# If x isn't a perfect square, we'll still draw floor(sqrt(x)) and note it
perfect = (n * n == x)

# --- drawing settings ---
SIZE = 30   # side length of each small square (pixels)
GAP  = 4    # space between squares (pixels)

# --- helpers ---
def draw_unit_square(t, size):
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.penup()

def draw_grid(t, n, size=30, gap=4):
    total = n * size + (n - 1) * gap
    start_x = -total / 2
    start_y =  total / 2  # top-left origin

    for r in range(n):
        for c in range(n):
            x = start_x + c * (size + gap)
            y = start_y - r * (size + gap)
            t.goto(x, y)
            draw_unit_square(t, size)

# --- turtle setup ---
wn = trtl.Screen()
t = trtl.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
t.penup()

# --- draw ---
draw_grid(t, n, SIZE, GAP)

# --- label ---
label = trtl.Turtle()
label.hideturtle()
label.penup()
total_side = n * SIZE + (n - 1) * GAP
label.goto(0, -total_side/2 - 30)

if perfect:
    label.write(f"√{x} = {n}  →  {n}×{n} squares", align="center", font=("Arial", 14, "normal"))
else:
    label.write(f"√{x} ≈ {n}  (not a perfect square)  →  drawing {n}×{n}", align="center", font=("Arial", 14, "normal"))

wn.mainloop()

