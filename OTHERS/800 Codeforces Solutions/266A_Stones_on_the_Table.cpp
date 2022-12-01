//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    string s;
    cin>>s;
    if(!n){ cout<<0<<endl;return 0;}

    int count=0;
    for(int i=0;i<n-1;i++){
        if(s[i]==s[i+1])
        count++;

    }
    cout<<count<<endl;
    return 0;
}