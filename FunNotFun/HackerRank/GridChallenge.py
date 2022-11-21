
# link: https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge


def gridChallenge(grid):
    # grid = ['abc','ade','efg']
    # sort the rows
    res = [sorted(g) for g in grid]
    print(res)
    # get columns
    res_t = [list(x) for x in zip(*res)]
    print(res_t)
    test_res_t = [sorted(t) for t in res_t]
    if res == sorted(res) and res_t == test_res_t:
        return 'YES'
    else:
        return 'NO'