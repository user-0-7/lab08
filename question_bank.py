#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Animal": [("What animal can change colors to blend in?", "Chameleon"),
        ("Which animal is the largest mammal on Earth?", "Blue Whale"),
        ("What animal is called man’s best friend?", "Dog"),
        ("Which animal builds dams in rivers?", "Beaver"),
        ("What’s the fastest land animal?", "Cheetah"),
        ("Which mammal can fly?", "Bat"),
        ("What animal has a long neck and lives in Africa?", "Giraffe"),
        ("Which animal eats mostly bamboo and has black-and-white fur?", "Panda"),
        ("What animal is known for carrying heavy loads, often in deserts?", "Camel"),
        ("Which animal has eight tentacles and can escape from tanks?", "Octopus"),
        # Add more questions as tuples (question, answer)
    ]
}

hints = {
    "Animal": ["Known for camouflaging in deserts and rainforests.",
        "A marine mammal with long migrations.",
        "Known for loyalty and often kept as a pet.",
        "A rodent with large teeth, known for engineering.",
        "A big cat that can reach 70 mph in short bursts.",
        "Often seen around Halloween and is nocturnal.",
        "The tallest land animal, munches on high trees.",
        "Native to China and a symbol of conservation.",
        "Famous for its strength.",
        "A cephalopod that can change its color."
        # Pair each question with a corresponding hint.
    ]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    p= player_answer
    c= correct_answer
    return p==c
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    for i in range(len(questions[category])):
                   if questions[category][i][0]==question:
                       questions.pop(i)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    print(display)
    answer= input().strip()
    return answer
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------
#####################################################check#############################

#---------------------------------------




