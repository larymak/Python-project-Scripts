//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin>>s;
    int u=0,l=0;
    for(auto x:s){
        if(isupper(x)) u++;
        else l++;
    }
    if(u>l){
        transform(s.begin(),s.end(),s.begin(),::toupper);
    }else transform(s.begin(),s.end(),s.begin(),::tolower);
    cout<<s<<endl;
    return 0;
}