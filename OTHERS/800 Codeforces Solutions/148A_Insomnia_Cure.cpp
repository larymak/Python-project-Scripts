//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform
#include<bits/stdc++.h>
using namespace std;

int main(){
    int a[4],d;
    cin>>a[0]>>a[1]>>a[2]>>a[3]>>d;
    int j;
    set<int> s;
    for(int i=0;i<4;i++){
        j=1;
        while(a[i]*j<=d){
            if(a[i]*j<=d) s.insert(a[i]*j);
            j++;
        }
    }
    cout<<s.size()<<endl;
    return 0;
}