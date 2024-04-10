login = {
    "username": "PGR107",
    "password": "Python"
}
questions = {
    0: {
        "question": "What is the capital of Norway?",
        "answer": "Oslo",
        "options": ["Bergen", "Oslo", "Stavanger", "Trondheim"]
        },
    1: {
        "question": "What is the currency of Norway??",
        "answer": "Krone",
        "options": ["Euro", "Pound", "Krone", "Deutsche Mark"]
        },
    2: {
        "question": "What is the largest city in Norway?",
        "answer": "Oslo",
        "options": ["Oslo", "Stavanger", "Bergen", "Trondheim"]
    },
    3: {
        "question": "When is constitution day (the national day) of Norway?",
        "answer": "17th May",
        "options": ["27th May", "17th May", "17th May", "27th April"]
        },
    4: {
        "question": "What color is the background of the Norwegian flag?",
        "answer": "Red",
        "options": ["Red", "White", "Blue", "Yellow"]
        },
    5: {
        "question": "How many countries does Norway border?",
        "answer": "3",
        "options": ["1", "2", "3", "4"]
        },
    6: {
        "question": "What is the name of the university in Trondheim?",
        "answer": "NTNU",
        "options": ["UiS", "UiO", "NMBU", "NTNU"]
        },
    7: {
        "question": "How long is the border between Norway and Russia?",
        "answer": "196 km",
        "options": ["96 km", "196 km", "296 km", "396 km"]
        
        },
    8: {
        "question": "Where in Norway is Stavanger?",
        "answer": "South-west",
        "options": ["North", "South", "South-west", "South-east"]
        },
    9: {
        "question": "From which Norwegian city did the world’s famous composer Edvard Grieg come?",
        "answer": "Bergen",
        "options": ["Oslo", "Bergen", "Stavanger", "Tromsø"]
        },
}
userAnswers = []
score = 0

def login_info(correct_info, username, password):
    if correct_info["username"] == username and correct_info["password"] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username and/or password!")
        return False

def printAlternatives(alt):
    for i in range(alt.__len__()):
        print(f"{i+1}. {alt[i]}")

def askQuestion(num):
    global score
    while True:
        print(questions[num]["question"])
        printAlternatives(questions[num]["options"])
        answer = input("Enter your answer: ")
        answer = int(answer)
    
        if answer>4 or answer<1:
            print("Invalid input")
            continue
        
        if questions[num]["options"][answer-1] == questions[num]["answer"]:
            score += 1
            return True
        else:
            userAnswers.append({"question":num,"userAnswer":questions[num]["options"][answer-1]})
            return False
    
def printUserAnswers():
    for i in range(userAnswers.__len__()):
        print(f"question: {questions[userAnswers[i]['question']]['question']}")
        print(f"Your answer: {userAnswers[i]['userAnswer']}")
        print(f"Correct answer: {questions[userAnswers[i]['question']]['answer']}")

def start():
    while True:
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
        if login_info(login,input_username , input_password):
            break
        else:
            continue
    
    for i in range(questions.__len__()):
        if askQuestion(i):
            print("Correct!")
        else:
            print("Wrong!")

    print(f"Your score: {score}/{questions.__len__()}")

    printUserAnswers()
        
start()