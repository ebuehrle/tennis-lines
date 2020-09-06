opt_partial_lines = [0, 1, 2, 3, 6, 5, 4, 5, 13, 14, 13, 8, 7, 8, 9, 12, 11, 10, 7, 4, 1, 0]
opt_full_lines = [0, 1, 10, 12, 9, 7, 8, 5, 14, 13, 4, 6, 3, 1, 0]
subopt_full_lines = [0, 1, 3, 6, 4, 1, 10, 12, 8, 5, 13, 14, 9, 7, 0]

import tennis
import visualization
import turtle

visualization.plot_court(tennis.vertices, tennis.lines)
visualization.plot_vertices(tennis.vertices)
turtle.getscreen().getcanvas().postscript(file='vertices.eps')

visualization.plot_solution(tennis.vertices, tennis.lines, opt_partial_lines)
tutle.getscreen().getcanvas().postscript(file='full.eps')

visualization.plot_solution(tennis.vertices, tennis.lines, reversed(opt_full_lines))
turtle.getscreen().getcanvas().postscript(file='partial.eps')

import matplotlib.pyplot as plt
plt.plot(tennis.incremental_path_cost(opt_full_lines))
plt.plot(tennis.incremental_path_cost(subopt_full_lines))
plt.xlabel('Step')
plt.ylabel('Accumulated Distance')
plt.show()
