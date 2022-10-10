//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin>>n;
    long long count=0;
    while(n!=0){
        int x=n%10;
        n/=10;
        if(x==4 || x==7){
            count++;
        }
    }
    if(count==0) {
        cout<<"NO"<<endl;
        return 0;
    }
    bool flag=true;
    while(count!=0){
        int x=count%10;
        count/=10;
        if(x!=4 && x!=7){
            flag=false;
            cout<<"NO"<<endl;
            break;
        }
    }
    if(flag) cout<<"YES"<<endl;
    return 0;
}