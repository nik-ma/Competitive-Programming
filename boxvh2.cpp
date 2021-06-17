#include<bits/stdc++.h>
using namespace std; 
typedef long long ll;
typedef unsigned long long ull;
#define rep(i,a,b) for(auto i=a;i<b;i++)
#define repD(i,a,b) for(auto i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define vi vector<int>
#define vll vector<ll>
#define FASTIO ios_base::sync_with_stdio(false);cin.tie(NULL);
int main()
{
	ull n,i,k,ans;
	cin>>n>>k;
	ull num[n+1];
	for(i=0;i<n;i++){
		cin>>num[i];
	}
	/* for(i=0;i<n;i++){
		cout<<num[i]<<" ";
	} */
	ull dif[n+1];
	for(i=0;i<n-1;i++){
		dif[i]=num[i+1]-num[i];
	}
	ans=num[n-1]-num[0];
	sort(dif+1,dif+n-1);
	ull s=0;
	
	cout<<ans;
	return 0;
}

