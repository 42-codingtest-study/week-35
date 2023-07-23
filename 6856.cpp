#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(0), cout.tie(0)
#define ll long long

int main()
{
    fast;
    int n, m;
    cin >> n >> m;
    int _min = min(n, m);
    int _max = max(n, m);
    int ans = 0;
    for (int i = 1; i <= _min; i++)
    {
        if (10 - i > 0 && 10 - i <= _max)
            ans++;
    }
    if (ans == 1)
        cout << "There is " << ans << " way to get the sum 10." << std::endl;
    else
        cout << "There are " << ans << " ways to get the sum 10." << std::endl;
}
