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
