StudentList1 = input().split(',')
StudentList2 = input().split(',')
StudentSet1,StudentSet2 = set(StudentList1), set(StudentList2)

set1 = StudentSet1&StudentSet2
#得到同时出现在两份名单中的人
set2 = StudentSet1|StudentSet2 #得到两份名单中的所有人
print(sorted(list(set1)))
print(sorted(list(set2)))

