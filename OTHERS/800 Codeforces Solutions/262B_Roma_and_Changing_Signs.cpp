// Problem: B. Roma and Changing Signs
// Contest: Codeforces - Codeforces Round #160 (Div. 2)
// URL: https://codeforces.com/contest/262/problem/B
// Memory Limit: 256 MB
// Time Limit: 2000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define FAST1 ios_base::sync_with_stdio(false);
#define FAST2 cin.tie(NULL);


int main(){
    FAST1;
    FAST2;
    int n;int k;
    cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++)
    	cin>>arr[i];
    
    int mn =INT_MAX;
    int sm=0; 
    for(int i=0;i<n;i++)
    {
    	mn = min(abs(arr[i]),mn);
    	if(arr[i]<0 && k>0)
    		arr[i] *= -1,k--;
    	sm+=arr[i];	
    }
    if(k>0 && k%2==1)
    	sm -= 2 * mn;
    	
    cout<<sm;
    return 0;
}
