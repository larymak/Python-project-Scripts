//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int total=0;
    int min=0;
    while(n--){
        int x;
        cin>>x;
        total-=x;
        cin>>x;
        total+=x;
        if(total>min)
        min=total;
    }
    cout<<min<<endl;
    return 0;
}