#include<iostream>
using namespace std;

int main()
{
    double n,i,c,f=0,s=1,sum;
    cout<<"Enter n: ";
    cin>>n;
    if(n==1)
    cout<<f;
    else if(n==2)
    cout<<s;
    else
    {
        c=2;
        for(i=2;i<n;i++)
        {
            c++;
            sum=f+s;
            f=s;
            s=sum;
            if(c==n)
            cout<<sum;       
        }
    }
    return 0;
}