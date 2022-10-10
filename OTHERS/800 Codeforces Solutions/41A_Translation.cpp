//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    string a,b;
    cin>>a>>b;
    for(int i=0;i<a.length()/2;i++){
        swap(a[i],a[a.length()-1-i]);
    }
    if(a==b) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
    return 0;
}