// code by Susritha
// cf handle:Susritha.S

#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
using namespace std;
int main(){
ll t;
cin>>t;
while(t--){
  ll n;
  cin>>n;
  ll a[n],i,j;
  ll sus=0;
  for(i=0;i<n;i++){
      cin>>a[i];
  }
  for(i=0;i<n;i++){
      while(a[i]>n){
          a[i]/=2;
      }
  }
  sort(a,a+n);
  map<ll,ll>m;
  for(i=0;i<n;i++){
 if(m[a[i]]==0){
     m[a[i]]++;
 }
 else{
     while(a[i]>0){
         if(m[a[i]]==0){
         m[a[i]]++;
         break;}
         else{
             a[i]/=2;
         }
         
     }
     if(a[i]==0){
         sus=1;
         break;
     }
 }
  }
  for(auto it=m.begin();it!=m.end();it++){
      if(it->second==0){
          sus=1;
          break;
      }
  }
  if(sus==0){
      cout<<"YES"<<endl;
  }
  else{
      cout<<"NO"<<endl;
  }
}
}
