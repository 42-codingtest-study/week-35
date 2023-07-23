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
    vector<bool> check(100, false);

    int a, b, c, d;
    cin >> a >> b >> c >> d;

    for (int i = a; i < b; i++)
        check[i] = true;
    for (int i = c; i < d; i++)
        check[i] = true;

    int ans = 0;
    for (int i = 0; i < 100; i++)
        if (check[i])
            ans++;

    cout << ans << "\n";
}
