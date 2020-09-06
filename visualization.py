import turtle

PX_PER_M_X = 65
PX_PER_M_Y = 65
ORIGIN_PX = (-310, -310)

COURT_COLOR = '#B73125'
LINE_COLOR = '#FFFFFF'
PATH_COLOR = '#AAAA00'

LINE_WIDTH = 3

def vertex2pos(v):
    return (ORIGIN_PX[0] + v[0] * PX_PER_M_X, ORIGIN_PX[1] + v[1] * PX_PER_M_Y)

def arrowarc(p0, p1, r_factor, label=''):
    import math
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    d = (dx**2 + dy**2) ** 0.5
    r = (1 + r_factor) * d / 2

    turtle.penup()
    turtle.goto(p0)
    turtle.pendown()
    turtle.setheading(turtle.towards(p1))

    half_angle = math.degrees(math.asin(d/(2*r)))
    turtle.left(half_angle)
    turtle.circle(-r, half_angle)
    turtle.stamp()
    turtle.write(label, font=('Arial', 32, "normal"))
    turtle.circle(-r, half_angle)
    #turtle.stamp()

def plot_vertices(vertices):
    turtle.shape('square')
    turtle.penup()
    for v in vertices:
        turtle.goto(vertex2pos(v))
        turtle.stamp()

def plot_lines(vertices, lines):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.color(LINE_COLOR)
    turtle.pensize(LINE_WIDTH)
    for l in lines:
        v0 = vertices[l[0]]
        v1 = vertices[l[1]]
        p0 = vertex2pos(v0)
        p1 = vertex2pos(v1)
        turtle.penup()
        turtle.goto(p0)
        turtle.pendown()
        turtle.goto(p1)

def plot_court(vertices, lines):
    turtle.clear()
    turtle.bgcolor(COURT_COLOR)
    plot_lines(vertices, lines)

def plot_path(vertices, path):
    turtle.shape('arrow')
    turtle.color(PATH_COLOR)
    
    for i, p in enumerate(path):
        if i == 0:
            turtle.penup()
            turtle.goto(vertex2pos(vertices[p]))
            turtle.pendown()
            continue

        v = vertices[p]
        arrowarc(turtle.pos(), vertex2pos(v), 2, i)

def plot_solution(vertices, lines, path):
    plot_court(vertices, lines)
    plot_vertices(vertices)
    plot_path(vertices, path)