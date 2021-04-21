#include <iostream>
#define NAME "newnum."
using namespace std;
int main()
{
	int m,d=0,d1,flg=0;
	string s;
 	cin>>s; 
	m=s.size();
 	for(int i=0;i<m;++i)
		d+=s[i]-48;
 	d%=3; 
	d1=3-d;
 	for(int i=0;i<m;++i)
	 	if(s[i]-48+d1<=9)
 		{
			flg=1;
		 	while(s[i]+d1<=57)
		 		s[i]+=d1,d1=3;
		 		break;
		}
 		if(flg==0)
			for(int i=m-1;i>=0;--i)
 				if(s[i]-48-d>=0)
				{
					s[i]-=d;
					break;
				}
	cout<<s;
}