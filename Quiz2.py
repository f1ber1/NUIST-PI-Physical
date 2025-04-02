#NUIST Quiz Game in Python
#date: 2/4/25
#nade by Guo
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def quiz():
	print("Welcome to the python Quiz")
	print("Answer the following questions:")

#Questing and Answers
	questions = [
		"1.Which of the follwing is NOT A PYTHON DATA type? a.int b.float c.rational d.string e.bool\n",
		"2.Which of the following is NOT a built-in operation in Python?a.+ b.% c.abs() d.sqrt()\n",
		"3.In a mixed-type expression involving ints and floats,Python will convert?a floats to ints b.ints to strings c.floats and ints to strings d.ints to floats\n",
		"4.The best structure for implementing a multi-way decision in Python is? a.if b.if-else c.if-elif-else d.try\n",
		"5.What statement can be executed in the body of a loop to cause it to terminate? a.if b.exit c.continue d.break\n"
	]
#define questions
	answers=[
		"rational",
		"sqrt()",
		"ints to floats",
		"if-elif-else",
		"break"
	]
#define answers

	score = 0

#Ask questions
	for i in range(len(questions)):
		user_answer = input(questions[i]).strip().lower() #get answer
		if user_answer == answers[i].lower(): #boolean user enter
			GPIO.setup(17,GPIO.OUT)
			GPIO.output(17,GPIO.HIGH)
			print("Correst!")
			score += 1
			time.sleep(5)
			GPIO.output(17,GPIO.LOW)
		else:
			GPIO.setup(18,GPIO.OUT)
			GPIO.output(18,GPIO.HIGH)
			print("Incorrect!")
			time.sleep(5)
			GPIO.output(18,GPIO.LOW)
	print("\nQuiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")

quiz()
#run program
