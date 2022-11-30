//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    double a[n];
    double ans=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        ans+=a[i];
    }
    cout<<ans/n<<endl;
    
    return 0;
}