#include <bits/stdc++.h>
#include <cmath>
using namespace std;

#define ll long long int
#define space " "
#define for(i,l,n) for(int i=l;i<n;i++) 
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()

ll solve()
{
  ll n,x;
  cin>>n>>x;
  vector<ll>num(n);
  ll maxi=0,mini=0;
  for(i,0,n){
      cin>>num[i];
    //   cout<<num[i]<<space;
      maxi+=(num[i]+x-1)/(x);
      mini+=num[i];


  }
  cout<<(mini+x-1)/(x)<<space<<maxi<<endl;


  return 0;
}


int main()
{
    fast;
     ll t = 1;
     cin >> t;
     while(t--)
     {
          solve();
     }
     return 0;
}