<<<<<<< HEAD
import io

import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sheng = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
num = int(input())
left = (num - 2020) % 12
print(sheng[left])



=======
import io

import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sheng = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
num = int(input())
left = (num - 2020) % 12
print(sheng[left])



>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119

