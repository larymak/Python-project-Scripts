//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform
#include <bits/stdc++.h>
using namespace std;

int main()
{
    set<long long> s;
    int temp;
    int t = 4;
    while (t--)
    {
        cin >> temp;
        s.insert(temp);
    }
    cout<<4-s.size()<<endl;
    return 0;
}