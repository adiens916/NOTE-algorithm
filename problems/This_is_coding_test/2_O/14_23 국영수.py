N = int(input())

students = []
for i in range(N):
    name, kor, eng, mat = input().split()
    students.append((-int(kor), int(eng), -int(mat), name))

students.sort()
for i in range(N):
    print(students[i][3])
