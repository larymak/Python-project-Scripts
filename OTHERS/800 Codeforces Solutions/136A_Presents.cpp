//code by Nikhil Nagrale
//nikhilnagrale2 on EveryPlatform else nknagrale
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int temp;
        cin>>temp;
        v.push_back(temp);  
    }
    int a[n];
    int num=1;
    for(int x:v){
        a[x-1]=num;
        num++;
    }
    for(int x:a)
    cout<<x<<" ";
    return 0;
}