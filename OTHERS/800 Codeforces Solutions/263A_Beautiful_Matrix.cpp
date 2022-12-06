//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    int a[6][6];
    int n,x,y;
    for(int i=1;i<=5;i++){
        for(int j=1;j<=5;j++){
            cin>>n;
            if(n){
                x=i;
                y=j;
            }
        }
    }
    cout<<(abs(3-x)+abs(3-y))<<endl;
    return 0;
}