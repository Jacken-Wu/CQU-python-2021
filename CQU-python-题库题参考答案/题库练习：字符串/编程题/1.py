import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

sky = ['癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬']
ground = ['亥', '子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌']
animal = ['猪', '鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗']
year = int(input())

s = sky[(year - 3) % 10]
g = ground[(year - 3) % 12]
a = animal[(year - 3) % 12]

print('%s%s年' % (s, g))
print('%s年' % a)

