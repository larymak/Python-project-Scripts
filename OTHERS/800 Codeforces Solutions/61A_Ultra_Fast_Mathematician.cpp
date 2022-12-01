//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string a, b;
    cin >> a >> b;
    string v = "";
    for (int i = 0; i < a.length(); i++)
    {
        if (a[i] == b[i])
            v += "0";
        else
            v += "1";
    }
    cout << v << endl;
    return 0;
}