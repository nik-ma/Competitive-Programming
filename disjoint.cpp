#include<bits/stdc++.h>
using namespace std;
 
int parent[100001];
 
int find(int a)
{
	while(parent[a] > 0)
		a = parent[a];
 
	return a;
}
 
void Union(int a , int b)
{
	parent[a] += parent[b];		//adding size of set b to set a
	parent[b] = a;				//making a , parent of new set
}
 
 
int main()
{ 
    int tc;
    cin>>tc;
    while(tc--){
	int n , m , a , b;
	cin>>n;
    cin>>m;
 
	for(int i=0;i<=n;i++)
		parent[i] = -1;		//initializing
 
	while(m--)
	{
        long long int temp,arr[100001];
		cin>>a>>b;
        a=a+1;
        b=b+1;
     
        
		a = find(a) , b = find(b);
 
		if(a != b) Union(a , b);
	}
 
	long long int res = 1;
 
	for(int i=1;i<=n;i++)
	if(parent[i] < 0)
	;
    }
}	