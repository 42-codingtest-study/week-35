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
    int h, m, s, hh, mm, ss;
    scanf("%d:%d:%d", &h, &m, &s);
    scanf("%d:%d:%d", &hh, &mm, &ss);
    int a = h * 60 * 60 + m * 60 + s;
    int b = hh * 60 * 60 + mm * 60 + ss;

    if (b <= a)
        b += 24 * 60 * 60;

    int diff = b - a;

    printf("%02d:%02d:%02d\n", diff / 60 / 60, (diff % (60 * 60)) / 60, diff % 60);
}
