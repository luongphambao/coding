#include<iostream>
#include<string>
#include<vector> 
using namespace std;
std::vector<int> spinackGraw(std::vector<int> spinack, std::vector<std::vector<int>> t)
{
    int t_size=t.size();
    int s_size=spinack.size();

    vector<char> a(s_size+1);
    for(int i=0; i<t_size; i++){
        a[t[i][1]+1]^=1;
        a[t[i][0]]^=1;
    }

    bool s=false;
    for(int i=s_size-1; i>=0; i--){
        s^=a[i+1];
        spinack[i]^=s;
    }  
    return spinack;
}