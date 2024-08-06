S = input()
Q = int(input())
inv = False
from collections import deque
S_deque = deque()
for num in range(len(S)):
  S_deque.append(S[num])

for i in range(Q):
  TFC = list(map(str, input().split()))
  if TFC[0] == "1":
    if inv == False:
      inv = True
    else:
      inv = False
  else:
    F = TFC[1]
    C = TFC[2]

    if inv == False:
      if F == "1":
        S_deque.appendleft(C)
      else:
        S_deque.append(C)
    else:
      if F == "1":
        S_deque.append(C)
      else:
        S_deque.appendleft(C)
ans = "".join(S_deque)

if inv == True:
  ans = ans[::-1]

print(ans)
    
    
#実行時間超過
    # S = input()
    # Q = int(input())
    # ans_list = []
    # ans_list.append(S)

    # for num in range(Q):
    # TFC = list(map(str, input().split()))

    # if TFC[0] == "1":
    #     #文字列反転
    #     ans_list = list(reversed(ans_list))
    # else:
    #     if TFC[1] == "1":
    #     #文字列 S の先頭に Ci​ を追加する。
    #     ans_list.insert(0, TFC[2])
    #     else:
    #     # Fi​=2 のとき : 文字列 S の末尾に Ci​ を追加する。
    #     ans_list.append(TFC[2])

    # ans = "".join(ans_list)
    # print(ans)