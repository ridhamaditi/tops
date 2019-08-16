def studentGrades(grades):
	if isinstance(grades, list):
		try:
			avg = list()
			for i in grades[1:]:
				a = 0
				for j in i[1:]:
					a += j
				a //= len(i) - 1
				avg.append(a)
			return avg
		except:
			return "'error'"
	else:
		return "'error'"

grades = [['Student']]
n = int(input("How many students? "))
quizes = int(input("How many quizes? "))
for i in range(1, quizes + 1):
	grades[0].append("Quiz " + str(i))
for i in range(n):
	student = list()
	student.append(input("Name: "))
	print("Marks: ")
	for i in range(quizes):
		student.append(int(input()))
	grades.append(student)
msg = studentGrades(grades)
print("\n", msg)