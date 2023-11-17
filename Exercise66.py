counter = 0
print("This program will calculate your grade point average (GPA) please enter grades such as A+, A, A-, B+, B, B-, C+,C,C-, D+, D-, F")
number = int(input("How many grades would you like to enter?: "))
totalScore = 0
while counter < number:
  grade = input("Enter your grade: ")
  if grade == "A+":
    totalScore = totalScore + 4.0
  if grade == "A":
    totalScore = totalScore + 4.0
  if grade == "A-":
    totalScore = totalScore + 3.7
  if grade == "B+":
    totalScore = totalScore + 3.3
  if grade == "B":
    totalScore = totalScore + 3.0
  if grade == "B-":
    totalScore = totalScore + 2.7
  if grade == "C+":
    totalScore = totalScore + 2.3
  if grade == "C":
    totalScore = totalScore + 2.0
  if grade == "C-":
    totalScore = totalScore + 1.7
  if grade == "D+":
    totalScore = totalScore + 1.3
  if grade == "D":
    totalScore = totalScore + 1.0
  if grade == "F":
    totalScore = totalScore + 0.0
  counter = counter + 1
finalGrade = totalScore/number
print("your GPA is:", finalGrade)