import functools
import bitsets

from dimensions import vertices
from dimensions import full_lines as lines
Lines = bitsets.bitset('Lines', tuple(lines))

def distance(v1, v2):
    dx = v2[0] - v1[0]
    dy = v2[1] - v1[1]
    return (dx**2 + dy**2) ** 0.5

def get_remaining_lines(lines, vidx1, vidx2):
    if not lines:
        return lines
    if (vidx1, vidx2) in lines.members():
        return lines.difference(Lines([(vidx1, vidx2)]))
    if (vidx2, vidx1) in lines.members():
        return lines.difference(Lines([(vidx2, vidx1)]))
    return lines

@functools.lru_cache(300000)
def fastest_tour(lines, start_vertex_idx, must_take_line):
    print("Lines:", lines, "Vertex:", start_vertex_idx, "Take Line:", must_take_line)

    if not lines:
        return (distance(vertices[start_vertex_idx], vertices[0]), 0, False)
    
    min_cost, min_vertex, min_take_line = float('inf'), -1, False
    for vidx in {v[0] for v in lines} | {v[1] for v in lines}: # only consider vertices incident to remaining lines
    #for vidx, _ in enumerate(vertices):
        if vidx == start_vertex_idx:
            continue
        
        remaining_lines = get_remaining_lines(lines, start_vertex_idx, vidx)
        took_line = (remaining_lines != lines)
        if must_take_line and not took_line:
            continue # taking no line more than once is always suboptimal
        
        (cost, _, _) = fastest_tour(remaining_lines, vidx, not took_line)
        cost += distance(vertices[start_vertex_idx], vertices[vidx])

        if cost < min_cost:
            min_cost = cost
            min_vertex = vidx
            min_take_line = must_take_line
    
    return (min_cost, min_vertex, min_take_line)

def incremental_path_cost(path):
    if len(path) == 1:
        return [0]
    elif len(path) > 1:
        inc_sub_cost = incremental_path_cost(path[:-1])
        return inc_sub_cost + [inc_sub_cost[-1] + distance(vertices[path[-2]], vertices[path[-1]])]

def reconstruct_path():
    lines = Lines.supremum
    must_take_line = False
    opt_path = [0]
    while True:
        (_, next_vidx, must_take_line) = fastest_tour(lines, opt_path[-1], must_take_line)
        opt_path.append(next_vidx)
        lines = get_remaining_lines(lines, opt_path[-2], opt_path[-1])
        if next_vidx == 0:
            break
    
    return opt_path

def main():
    opt_path = reconstruct_path()
    print(opt_path)

if __name__ == '__main__':
    main()

