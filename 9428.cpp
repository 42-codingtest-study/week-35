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
    int N;
    cin >> N;

    while (N--)
    {
        int iM, iY, sM, sY;
        cin >> iM >> iY >> sM >> sY;

        double EIT = 0;
        if (iY == sY)
        {
            EIT += 0.5 * (sM - iM) / (12.0 - iM + 1);
        }
        else
        {
            EIT += 0.5 + (sY - iY - 1) + (sM - 1) / 12.0;
        }

        cout << fixed;
        cout.precision(4);
        cout << EIT << endl;
    }
}
