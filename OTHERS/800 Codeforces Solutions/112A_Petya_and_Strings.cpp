//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    string a,b;
    cin>>a>>b;
    for(auto &c: a) c=tolower(c);
    transform(b.begin(),b.end(),b.begin(),::tolower);
    cout<<a.compare(b)<<endl;
    return 0;
}