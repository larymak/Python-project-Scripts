//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> v;
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i != j && v[i].first == v[j].second)
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}

//O(n+m) solution is also possible