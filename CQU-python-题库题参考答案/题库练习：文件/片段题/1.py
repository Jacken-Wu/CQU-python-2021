"""
输入学生个人信息并写入到文件data.txt中。
"""
f = open('data.txt', 'w+')

f.write("sno\tsname\tsage\n")
stext = input() or "End"
while stext != "End":
    stu = stext.split(",")
    f.write('%s\t%s\t%s\n' % tuple(stu))

    stext = input() or "End"
f.seek(0)
print(f.read())
f.close()




