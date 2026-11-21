def show_percentage(percentage):

        if percentage >=90:
            print("You nailed it!")
        elif percentage >=80:
            print(" did well!")
        elif percentage >=70:
            print("Good job!")
        elif percentage >=60:
            print(" do better!")
        elif percentage >=50:
            print("need to work hard!") 
        elif percentage >=40:
            print("work hard!")
        elif percentage >=30:
            print("failed :( ")
        else:
            print("failed :("   )
score = 0
counter = 0
quiz = {
    "What does RAM stand for?": "random access memory",
    "What does GPU stands for?": "Graphic processing unit",
    "what is the full from of SQL?": "structured query language",
    "what is the full form of HTML?": "Hypertext markup language",
    "Who is the founder of openAI?": "Sam Altman",
    "who is known as the father of computer science?": "Alan Turing",
    "who is known as the father of computer?": "Charles Babbage",

}
total_questions = len(quiz)

for question, answer in quiz.items():
    counter += 1
    print(f"\nQuestion {counter}/{total_questions}")
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("correct answer!")
        score += 1
        else:
            print("wrong answer!")
            print("The correct answer is:", answer)

percentage = (score / total_questions) * 100
print("Quiz Finished!")
print(f"Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")
    show_percentage(percentage)

