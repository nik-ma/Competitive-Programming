#include<iostream>
#include<stdio.h>
#include<string>
int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	int TC;
	std::cin>>TC;
	for(int c=0; c<TC; c++)
	{
		int n,x=0, y=0;
		char px = 'k';
		std::cin>>n;
		std::string sn;
		std::cin>>sn;
		std::string::iterator i=sn.begin();
		for(i; i!=sn.end(); ++i)
		{
			if((px=='y'&&(*i=='L' || *i=='R'))||(px=='x'&&(*i=='U' || *i=='D')))
				continue;
			else if(*i == 'L')
			{
				x--;
				px = 'y';
			}
			else if(*i == 'R')
			{
				x++;
				px = 'y';;
			}
			else if(*i == 'U')
			{
				y++;
				px = 'x';;
			}
			else if(*i == 'D')
			{
				y--;
				px = 'x';;
			}
		}
		std::cout<<x<<" "<<y<<"\n";
	}
}