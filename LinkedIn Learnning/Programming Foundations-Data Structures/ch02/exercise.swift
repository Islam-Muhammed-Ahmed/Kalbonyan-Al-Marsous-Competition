var perStudentPetCount = [0, 1, 2, 0, 1, 1, 4, 0, 0, 5, 0]

var numOfStudents = perStudentPetCount.count

print(perStudentPetCount[2])
print(numOfStudents)

var sum = 0
for individualStudent in perStudentPetCount{
    sum += individualStudent
}

print(sum)

print("average is ", sum / numOfStudents)