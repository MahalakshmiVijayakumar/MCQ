import time

score = 0

# ANSI escape sequences for colors
class colors:
    QUESTION = '\033[94m'  # Blue
    ANSWER = '\033[92m'  # Green
    HINT = '\033[93m'  # Yellow
    TIMEUP = '\033[91m'  # Red
    WRONG = '\033[91m'  # Red
    SCORE = '\033[96m'  # Cyan
    HIGHEST_SCORE = '\033[95m'  # Magenta
    END = '\033[0m'  # End of color

def get_option_input(prompt, hint, hint_provided, time_limit):
    start_time = time.time()
    while True:
        if hint_provided:
            answer = input(f"{colors.QUESTION}{prompt}\n{colors.HINT}Hint: {hint}\n{colors.ANSWER}Your answer is: {colors.END}")
        else:
            answer = input(f"{colors.QUESTION}{prompt}\n{colors.HINT}Hint:\n{colors.ANSWER}Your answer is: {colors.END}")
        
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            print(f"{colors.TIMEUP}Time's up! You took too long (more than {time_limit} seconds).{colors.END}")
            return None
        
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print(f"{colors.WRONG}Invalid input! Please enter a valid option (A, B, C, or D){colors.END}")

def add_question():
    question_text = input("Enter the question text: ")
    options = []
    for option in ['A', 'B', 'C', 'D']:
        options.append(input(f"Enter option {option}: "))
    correct_answer = input("Enter the correct option (A, B, C, or D): ").upper()
    hint = input("Enter a hint for this question: ")
    questions.append((f"{len(questions) + 1}. {question_text}\n A. {options[0]}\n B. {options[1]}\n C. {options[2]}\n D. {options[3]}", hint))
    correct_answers.append(correct_answer)

questions = [
    ("1. What is the addition of 4 and 5:\n A. 5\n B. 9\n C. 8\n D. 11", "Think of the sum of 4 and 5"),
    ("2. What is the name of chemical formula O:\n A. Magnesium\n B. Calcium\n C. Oxygen\n D. Neon", "It's essential for breathing"),
    ("3. What is the National Bird of India:\n A. Peacock\n B. Parrot\n C. Penguin\n D. Pigeon", "It's known for its colorful feathers"),
    ("4. What is the color of Peace:\n A. Yellow\n B. Green\n C. Blue\n D. White", "It's the color of doves"),
    ("5. What is the powerhouse of the cell?:\n A. Ribosome\n B. Mitochondrion\n C. Golgi apparatus\n D. Endoplasmic reticulum", "It's known for energy production"),
    ("6. What is the capital city of Australia?:\n A. Melbourne\n B. Sydney\n C. Canberra\n D. Brisbane", "It's neither the largest nor the most famous city in Australia"),
    ("7. Which of the following is a fundamental force of nature?:\n A. Friction\n B. Tension\n C. Gravity\n D. Buoyancy", "It pulls objects toward the Earth"),
    ("8. What does GDP stand for?:\n A. General Domestic Product\n B. Gross Domestic Product\n C. Grand Development Plan\n D. Gross Development Price", "It's a measure of a country's economic performance"),
    ("9. Who is considered the Father of Modern Political Science?:\n A. Aristotle\n B. Niccolò Machiavelli\n C. John Locke\n D. Thomas Hobbes", "He wrote 'The Prince'"),
    ("10. What is the primary greenhouse gas emitted by human activities?:\n A. Methane\n B. Nitrous oxide\n C. Carbon dioxide\n D. Ozone", "It's a product of burning fossil fuels")
]

correct_answers = ['B', 'C', 'A', 'D', 'B', 'C', 'C', 'B', 'B', 'C']
time_limit = 10  # Time limit in seconds for each question

while True:
    add_question_choice = input("Do you want to add a new question? (yes/no): ").lower()
    if add_question_choice == 'yes':
        add_question()
    else:
        break

for i, (question, hint) in enumerate(questions):
    hint_provided = False
    answer = get_option_input(question, hint, hint_provided, time_limit)
    if answer is None:
        print(f"{colors.WRONG}Wrong! The correct answer is '{correct_answers[i]}'{colors.END}")
        score -= 1
        continue
    if answer == correct_answers[i]:
        print(f"{colors.ANSWER}Correct!{colors.END}")
        score += 1
    else:
        print(f"{colors.WRONG}Wrong! Try again.{colors.END}")
        hint_provided = True
        answer = get_option_input(question, hint, hint_provided, time_limit)
        if answer is None:
            print(f"{colors.WRONG}Wrong again! The correct answer is '{correct_answers[i]}'{colors.END}")
            score -= 1
            continue
        if answer == correct_answers[i]:
            print(f"{colors.ANSWER}Correct!{colors.END}")
            score += 1
        else:
            print(f"{colors.WRONG}Wrong again! The correct answer is '{correct_answers[i]}'{colors.END}")
            score -= 1

print(f"{colors.SCORE}Your total score is: {score}/{len(questions)}{colors.END}")
print(f"{colors.HIGHEST_SCORE}The Highest score is: {score}{colors.END}")




