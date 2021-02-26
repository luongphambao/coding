#define ff(i , a, b) for (int i = a; i <= b; i++)
#define REP(i , a ,b) for (int i =a; i>=b; i--)

typedef long long ll;
const ll base = 311;
const ll mode = 1e9 + 7;
const ll oo = 1e7;

long long sumOfOnes(long long n, long long l, long long r)
{
    l-- ; r--;

    if (n == 0) return  0;
    else if (n == 1) return 1;
    else
    {
        int logarit = log2(n);

        stack<ll> mod;
        while(n > 1)
        {
            mod.push(n%2);
               n/=2;
        }

        mod.push(1);

        stack<ll> lenth;

        REP(i , logarit , 1)
        {
           lenth.push(pow(2 , i));
        }

    //cout << lenth.size() << " " << mod.size() << endl;

        ll start = 0;
        ll total = 0;

        while(!lenth.empty())
        {
            ll in_begin = oo;

            if (l <= start) in_begin = start;
            else if ((l-start)%lenth.top() == 0) in_begin = l;
            else
            {
                in_begin = ((l-start)/lenth.top() + 1)*lenth.top() + start;
            }
            if (in_begin <= r && mod.top() == 1) total += (r-in_begin)/lenth.top() + 1;

            /*if (in_begin == oo) cout << -1 << " ";
            else cout << start << " " << lenth.top() << endl;*/
            //cout << in_begin << " ";

            start = (start + start + lenth.top())/2;

            lenth.pop();
            mod.pop();

    }

    ll number = pow(2 , logarit + 1) - 1;
    if ((number/2) >= l && (number/2) <= r && mod.top() == 1) total++;

    return total;

    }

}