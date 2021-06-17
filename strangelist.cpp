#include <bits/stdc++.h>
#include <cmath>
using namespace std;

// #define print(one) cout<<one; 
// #define print(one,space) cout<<one<<" ";
#define ll long long int
ll sumt=0;
#define space " "
#define for(i,l,n) for(int i=l;i<n;i++) 
#define fast ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define all(c) (c).begin(),(c).end()
#define sz(v) (int)(v).size()
ll calculate(vector< vector<ll> >&listi,ll x){
    ll n=listi.size(),z;
    cout<<"hello"<<n<<endl;
    for(i,0,n){
        cout<<listi[i][0]<<space<<listi[i][1]<<endl;
    }
    int flag=0;
    vector< vector<ll> >values;
    for(i,0,n){
        if(listi[i][1]%x==0){
            z=listi[i][0];
            sumt+=listi[i][0];
            values.push_back({z,listi[i][1]/x});
        }
        else
        {
            flag=1;
            break;
        } 
    }
    if(flag!=1){
        if(values.size()>0)
        {calculate(values,x);}
    }

}
ll solve()
{
  ll n,x,a,b,c,d,q,k,j,m,flag=0;
  sumt=0;
  cin>>n>>x;
    vector<ll>num(n);

  for(i,0,n){
      cin>>num[i];
      sumt+=num[i];
  }
vector< vector<ll> >listi;
for(i,0,n){
    if (num[i]%x==0){
        m=num[i];
        sumt+=num[i];
    
        listi.push_back({m,num[i]/x});
        // cout<<m<<space<<listi[1][0]<<space<<listi[0][1];
        }
    else
    {
        flag=1;
        break;
    }  
}
    if(flag==1){
        cout<<sumt<<endl;
    }
    else{
        n=listi.size();
        for(i,0,n){
        cout<<listi[i][0]<<space<<listi[i][1]<<endl;
    }

        calculate(listi,x);
        cout<<sumt<<endl;
    }

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