// Problem: A. Roma and Lucky Numbers
// Contest: Codeforces - Codeforces Round #160 (Div. 2)
// URL: https://codeforces.com/contest/262/problem/A
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// 
// Powered by CP Editor (https://cpeditor.org)

#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define FAST1 ios_base::sync_with_stdio(false);
#define FAST2 cin.tie(NULL);
int n, k, ans, num;
	string s;
int main(){
    FAST1;
    FAST2;
    
	cin >> n >> k;
	for (int i = 0; i < n; i++){
		cin >> s;
		for (int j = 0; j < s.size(); j++){
			if (s[j] == '7' || s[j] == '4'){
				num ++;
			}
		}
		if (num <= k){
			ans++;
		}
		num = 0;
	}
	cout << ans << endl;
	return 0;

}
