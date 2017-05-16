# -*- coding: utf-8 -*-
#
# [Lake Counting (POJ No.2386)]
# 大きさがN×Mの庭があります。そこに雨が降り、水溜りができました。水溜りは８近
# 傍で隣接している場合につながっているとみなします。全部でいくつの水溜りがある
# でしょうか？（８近傍とは、次のWに対する*の部分を指します）
#
# ***
# *W*
# ***
#
# <!>制約
#  N, M <= 100


def __is_valid_inputs(N, M):
    if N > 100:
        return False
    if M > 100:
        return False
    return True


def __dfs(x, y, n, rch, N, M, lake):
    if x < 0 or x >= N or y < 0 or y >= M:
        # this point is out of area
        return
    if rch[x][y] != -1:
        # this point was reached
        return
    if lake[x][y] == 0:
        # this point is not warter
        rch[x][y] = 0
        return
    # mark reach point
    rch[x][y] = n
    # check around this point
    for i in [x + k for k in (-1, 0, 1)]:
        for j in [y + k for k in (-1, 0, 1)]:
            __dfs(i, j, n, rch, N, M, lake)
    return


def __lake_count_dfs(N, M, lake):
    rch = [[-1] * M for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if rch[i][j] != -1:
                # this point was reached
                continue
            elif lake[i][j] == 0:
                # this point is not warter
                rch[i][j] = 0
                continue
            else:
                cnt += 1
                __dfs(i, j, cnt, rch, N, M, lake)
    return cnt


def lake_count(N, M, lake):
    if not __is_valid_inputs(N, M):
        return -1
    return __lake_count_dfs(N, M, lake)


if __name__ == "__main__":
    N = 10
    M = 12
    lake_map = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    assert lake_count(N, M, lake_map) == 3, "case true"
