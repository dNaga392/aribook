# -*- coding: utf-8 -*-
#
# [迷路の最短路]
# 大きさがN×Mの迷路が与えられます。迷路は通路と壁からできており、１ター
# ンに隣接する上下左右４マスの通路へ移動することができます。スタートから
# ゴールまで移動するのに必要な最小ターン数を求めなさい。ただし、スタート
# からゴールまで移動できると仮定します。
#
# <!>制約
#  N, M <= 100


def __get_pos_of(ch, field):
    for i, line in enumerate(field):
        if ch not in line:
            continue
        return (i, line.index(ch))
    return (-1, -1)


def __get_next_pos(N, M, maze, x, y):
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        i += x
        j += y
        if i < 0 or i >= N or j < 0 or j >= M:
            continue
        if maze[i][j] not in ('.', 'G'):
            continue
        yield (i, j)


def get_shortest_path(N, M, maze):
    start = __get_pos_of('S', maze)
    turn = 0
    points = {0: [start]}
    while turn in points.keys():
        for x, y in points[turn]:
            if maze[x][y] == 'G':
                return turn
            maze[x][y] = '*'
            nexts = list(__get_next_pos(N, M, maze, x, y))
            if len(nexts) == 0:
                continue
            if turn + 1 in points.keys():
                points[turn + 1].extend(nexts)
            else:
                points[turn + 1] = nexts
        turn += 1
    return -1


if __name__ == "__main__":
    N = 10
    M = 10
    maze_t = """#S######.#
                ......#..#
                .#.##.##.#
                .#........
                ##.##.####
                ....#....#
                .#######.#
                ....#.....
                .####.###.
                ....#...G#"""
    maze = [list(line) for line in maze_t.split()]
    assert get_shortest_path(N, M, maze) == 22, "example"
