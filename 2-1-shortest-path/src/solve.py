# -*- coding: utf-8 -*-
#
# [���H�̍ŒZ�H]
# �傫����N�~M�̖��H���^�����܂��B���H�͒ʘH�ƕǂ���ł��Ă���A�P�^�[
# ���ɗאڂ���㉺���E�S�}�X�̒ʘH�ֈړ����邱�Ƃ��ł��܂��B�X�^�[�g����
# �S�[���܂ňړ�����̂ɕK�v�ȍŏ��^�[���������߂Ȃ����B�������A�X�^�[�g
# ����S�[���܂ňړ��ł���Ɖ��肵�܂��B
#
# <!>����
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
