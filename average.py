#Initialaize all variables to 0
numberOfScores=0
score=0
total=0
scoreCount=0
average=0.0
# Accept the number of scores to average
numberOfScores=input("Please enter the number of scoures you want average:")
#Add a loop to make this code repeat until scoreCount = numberOfScores
#scoreCount less than numberOfScores
while (scoreCount!=numberOfScores):
	score=int(input("Please enter a score:"))
	total= total + score
	scoreCount=scoreCount + 1
	average=total / numberOfScores
