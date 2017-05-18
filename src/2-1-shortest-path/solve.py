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


def get_shortest_path(N, M, maze):
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
    maze = []
    for line in maze_t.split():
        maze.append(list(line))
    print(maze)
    assert get_shortest_path(N, M, maze) == 22, "example"
