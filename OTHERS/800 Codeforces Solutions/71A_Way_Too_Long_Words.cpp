//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    while(n--){
        string s;
        cin>>s;
        if(s.length()>10){
            string ans;
            ans.push_back(s.front());
            ans+=to_string(s.length()-2);
            ans+=s.back();
            cout<<ans<<endl;
        }else cout<<s<<endl;
    }
    return 0;
}