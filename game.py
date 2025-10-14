trivia = [
    {
        'question':'What is the name of the person on the joker joker in balatro?',
        'answer': 'Jimbo',
        'options': ['Joker', 'Jambob', 'Jimbo']
    },
    {
        'question': 'How many hours does it take to beat Terraria?',
        'answer': '230',
        'options': ['100', '60', '230']

    },

    {
        'question': 'What mob in minecraft is unused, but still in the game?',
        'answer': 'Giant',
        'options': ['Iceologer', 'Tuffle Golem', 'Giant']

    },
    {
        'question': 'What joker in balatro is the best?',
        'answer': 'None',
        'options': ['Blueprint', 'Yorick', 'None']

    },
    {
        'question': 'What is the maximum amount of torches you can carry in one slot in Darkest Dungeon?',
        'answer': '8',
        'options': ['16', '4', '8']

    },
    {
        'question': 'Can Radann be parried in Elden Ring?',
        'answer': 'No',
        'options': ['Maybe', 'Yes', 'No']

    },
    {
        'question': 'Why did Radann learn gravity magic?',
        'answer': 'To ride his horse',
        'options': ['He did not', 'To be cool', 'To ride his horse']

    },
    {
        'question': 'What does Mayor Lewis want to keep a secret?',
        'answer': 'his undies',
        'options': ['Tax evasion', 'Embezzling town money', 'His undies']

    },
]

def ask_q (question, answer, option):
    is_correct = False;
    #1. Display the questions
    print(question)
    #2. Display the options
    print(option)
    #3. Take user input
    user_answer = input(question)
    #4. Check if user input matches correct answer

    return is_correct
if (user_answer == answer):
 print("Correct! Onto the the next question:")


    
    

    


# Define functions to ask the questions and compute the score
# GAMER LOOP, call your functions below
def main():
    print("Starting a new Trivia game...")
    user_name = input("Enter your name already. I don't have time for this: ")
    print(f"Hello, {user_name}.")

    for q in trivia :
        question = q['question']
        answer = q['answer']
        options = q['options']
        ask_q(question, answer, options)



main()
