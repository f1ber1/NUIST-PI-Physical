#NUIST Quiz Game in Python
#date: 2/4/25
#nade by Guo

def quiz():
	print("Welcome to the Animal Quiz")
	print("Answer the following questions:")

#Questing and Answers
	questions = [
		"1.What is the largest animal on Earth?:a.Blue Whale,b.Mouse,c.Cat",
		"2.Which bird can fly backwards?:a.Cuckoo,b.Eagle,c.Hummingbird",
		"3.What is the only mammal capable of flight?:a.Bat,b.Squirrel,c.Dolphin"
	]
#define questions
	answers=[
		"Blue whale",
		"Hummingbird",
		"Bat"
	]
#define answers

	score = 0

#Ask questions
	for i in range(len(questions)):
		user_answer = input(questions[i]).strip().lower() #get answer
		if user_answer == answers[i].lower(): #boolean user enter
			print("Correst!")
			score += 1
		else:
			print("Incorrect!")
	print("\nQuiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")

quiz()
#run program
