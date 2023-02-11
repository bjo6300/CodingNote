# 생태학
## 다른사람 코드
import sys
input = sys.stdin.readline

trees = {}
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    n += 1
        
tree_lst = list(trees.keys())
tree_lst.sort()
for tree in tree_lst:
    print('%s %.4f' %(tree, trees[tree]/n*100))

## 이거 왜 틀림
# import sys
# input = sys.stdin.readline

# tree_dict = {}

# for _ in range(10000):
#     tree = input().rstrip()

#     if not tree:
#         break

#     if tree in tree_dict:
#         tree_dict[tree] += 1
#     else:
#         tree_dict[tree] = 1

# tree_dict = sorted(tree_dict.items(), key=lambda x:x[0])
# tree_dict2 = dict(tree_dict)

# a = sum(list(tree_dict2.values()))

# for i in tree_dict:
#     print(i[0], round(int(i[1])/a * 100, 4))
