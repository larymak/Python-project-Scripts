//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int count=0;
    while(n--){
        int x,y,z;
        cin>>x>>y>>z;
        if((x+y+z)>=2) count++;
    }
    cout<<count<<endl;
    return 0;
}