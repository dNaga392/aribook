#include <vector>

int calc_fall_ants_max_time(int L, int n, const std::vector<int> & x);
int calc_fall_ants_min_time(int L, int n, const std::vector<int> & x);
// array
template <std::size_t N>
int calc_fall_ants_max_time(int L, int n, const int (&x)[N])
{
    std::vector<int> v;
    for (unsigned i = 0; i < N; ++i)
    {
        v.push_back(x[i]);
    }
    return calc_fall_ants_max_time(L, n, v);
}
template <std::size_t N>
int calc_fall_ants_min_time(int L, int n, const int (&x)[N])
{
    std::vector<int> v;
    for (unsigned i = 0; i < N; ++i)
    {
        v.push_back(x[i]);
    }
    return calc_fall_ants_min_time(L, n, v);
}
