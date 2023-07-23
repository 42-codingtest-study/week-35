# code.plus - 차이를 최대로
# fail

import sys
from itertools import permutations

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split())) 

for i in permutations(data) :
  ans = 0
  for j in range(n - 1) :
    ans += abs(i[j] - i[j + 1])
  max_ans = max(max_ans,ans)

print(max_ans)