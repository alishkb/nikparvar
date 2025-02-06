import random
operators = ['+' , '-' , '×' , '÷']
counter = 1
score = 0
while True:
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(operators)
    
    question = str(number1) + ' ' + str(operator) + ' ' + str(number2)
    print(question)

    if operator == '+':
        answer = number1 + number2
        answer_list = []
        while len(answer_list) < 10:
            choice_obj = random.randint(number1 - 5 , number1 + 5) + number2
            if choice_obj != answer and choice_obj not in answer_list:
                answer_list.append(choice_obj)

    elif operator == '-':
        answer = number1 - number2
        answer_list = []
        while len(answer_list) < 10:
            choice_obj = random.randint(number1 - 5 , number1 + 5) - number2
            if choice_obj != answer and choice_obj not in answer_list:
                answer_list.append(choice_obj)

    elif operator == '×':
        answer = number1 * number2
        answer_list = []
        while len(answer_list) < 10:
            choice_obj = random.randint(number1 - 5 , number1 + 5) * number2
            if choice_obj != answer and choice_obj not in answer_list:
                answer_list.append(choice_obj)

    elif operator == '÷':
        answer = round(number1 / number2, 2)
        answer_list = []
        while len(answer_list) < 10:
            choice_obj = random.randint(number1 - 5 , number1 + 5) / number2
            if choice_obj != answer and choice_obj not in answer_list:
                answer_list.append(round(choice_obj, 2))



    show_choices = []
    while len(show_choices) < 3:
        show_choice = random.choice(answer_list)
        if show_choice not in show_choices:
            show_choices.append(show_choice)

    show_choices.insert(random.randint(0, 3), answer)

    print()
    print('answer this question is: ' + str(answer))
    print()

    # for j in answer_list:
    #     print(j)

    for j in range(1, 5):
        print(str(j) + '- ' + str(show_choices[j-1]))
        

    user_answer = input('Enter your answer choice (Type "exit" or "end" for end): ')
    if user_answer == 'end' or user_answer == 'exit':
        break

    while True:
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= 4:
                break
                
            print('Plaese enter a number between 0 and 5! Try again')
            user_answer = input('Enter your answer choice again: ')
            continue

        except ValueError:
            print('You can\'t enter string value! Try again')
            user_answer = input('Enter your answer choice again: ')


    if show_choices[user_answer-1] == answer:
        print('Your answer is True :)')
        if operator == '+' or operator == '-':
            score += 1

        elif operator == '×' or operator == '÷':
            score += 3


    else:
        print('Your answer is not True :(')
        break

    counter += 1

print("You answered " + str(counter) + ' questions')
print('Your score is: ' + str(score))