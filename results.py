opt_partial_lines = [0, 1, 2, 3, 6, 5, 4, 5, 13, 14, 13, 8, 7, 8, 9, 12, 11, 10, 7, 4, 1, 0] # 101.77m
opt_full_lines = [0, 1, 10, 12, 9, 7, 8, 5, 14, 13, 4, 6, 3, 1, 0] # 104.35m
subopt_full_lines = [0, 1, 3, 6, 4, 1, 10, 12, 8, 5, 13, 14, 9, 7, 0] # 107.87m

import tennis
import visualization
import turtle

def plot_vertices():
    visualization.plot_court(tennis.vertices, tennis.lines)
    visualization.plot_vertices(tennis.vertices)
    turtle.getscreen().getcanvas().postscript(file='vertices.eps')

def plot_measurements():
    plot_vertices()
    visualization.plot_vertical_measurement(tennis.vertices[1], tennis.vertices[3], '11.89m')
    visualization.plot_vertical_measurement(tennis.vertices[5], tennis.vertices[6], '6.40m')

    visualization.plot_horizontal_measurement(tennis.vertices[1], tennis.vertices[4], '1.37m')
    visualization.plot_horizontal_measurement(tennis.vertices[1], tennis.vertices[10], '10.97m', delta_y=-60)

    visualization.plot_vertical_measurement(tennis.vertices[0], tennis.vertices[1], '3m')
    visualization.plot_horizontal_measurement(tennis.vertices[0], tennis.vertices[1], '3m', delta_y=-60)
    turtle.getscreen().getcanvas().postscript(file='measurements.eps')

def plot_full_lines():
    visualization.plot_solution(tennis.vertices, tennis.lines, reversed(opt_full_lines))
    turtle.getscreen().getcanvas().postscript(file='full.eps')

def plot_partial_lines():
    visualization.plot_solution(tennis.vertices, tennis.lines, opt_partial_lines)
    turtle.getscreen().getcanvas().postscript(file='partial.eps')

def plot_compare_solution():
    import matplotlib.pyplot as plt
    plt.plot(tennis.incremental_path_cost(opt_full_lines))
    plt.plot(tennis.incremental_path_cost(subopt_full_lines))
    plt.xlabel('Step')
    plt.ylabel('Accumulated Distance in m')
    plt.savefig('compare.png')

if __name__ == '__main__':
    plot_vertices()
    plot_measurements()
    plot_full_lines()
    plot_partial_lines()
    #plot_compare_solution()
