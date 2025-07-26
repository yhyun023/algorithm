#include <iostream>
using namespace std;

int fac(int num){
    if ((num == 0)||(num == 1)){
        return 1;
    }
    else{
        return num * fac(num-1);
    }
}
int main(){
    int number;
    cin >> number;
    cout << fac(number) << endl;
    return 0;
}