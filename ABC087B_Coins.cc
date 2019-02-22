/*
あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。 
これらの硬貨の中から何枚かを選び、合計金額をちょうど X
円にする方法は何通りありますか。
同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨について
その硬貨を選ぶ枚数が異なるとき区別されます。

*/
#include <iostream>
using namespace std;

int main(){
    int X, A, B, C;
    int ans=0;

    scanf("%d\n", &A);
    scanf("%d\n", &B);
    scanf("%d\n", &C);
    scanf("%d\n", &X);
    
    for(int i = 0; i<=A;++i){
        for(int j =0; j<=B;++j){
            for(int k = 0; k<=C; ++k){
                if(X == 500*i +100*j + 50*k) ans++;
                else continue;
            }
        }
    }

    printf("%d\n", ans);
    return 0;
}