print "Welcome to The Drake Quiz! What is your name?"
name = raw_input("")

# asks for player's name
print "Hi " + name + "!" + " Its time to find out if you're a true Drake fan."


# the Drake quizzes in 3 difficulties
easy_quiz = ("""___1___ Drake Graham, born in ___2___, Canada, is a Canadian
rapper, singer-songwriter, record producer, and actor. His first acting gig was
a Canadian teen drama series called ___3___, where he played a basketball star
who became physically disabled after being shot by a classmate. His song Views
from the 6 was about his on and off relationship with the singer ___4___.""")

medium_quiz = ("""After releasing a few of his own mixtapes, Drake signed a
recording contract with Lil Wayne's lable, ___1___ Entertainment, in 2009.
However, he soon sought to release his own music as well as help in the
nuturing of other artists, creating his own label know as ___2___ Sound. Drake,
 also known as ___3___ God,  has produced a quadruple platnium album, hosted
 SNL and received a breaking record of 13 AMA Nominations all in 2016. Finally,
  he ended the year with his '___4___ Tour' with Future, totalling 54 shows
  around the US and Canada.""")

hard_quiz = ("""Drake, being half African American and half Caucasian, adopted
 his mother's ___1___ faith. He holds the record for most entries into the
 Billboard Hot 100 in one week with ___2___ entries, surpassing the Beatles and
  Justin Bieber. Although Drake does not have a huge presence on social media,
  his Instagram, also known as ___3___, amasses over 37.6M followers.
  Drake was named the most streamed artist by Spotify in 2016 and his song,
   ___4___, became Spotify's most streamed song.""")

# answers to the quizzes
easy_answer = ["Aubrey", "Toronto", "Degrassi", "Rihanna"]
medium_answer = ["Young Money", "OVO", "6", "Summer Sixteen"]
hard_answer = ["Jewish", "20", "champagnepapi", "One Dance"]
blanks = ["___1___", "___2___", "___3___", "___4___"]

def choose_difficulty():
    """
    Behavior: Chooses one of the three quizzes to take.
    Input: The player's desired difficulty.
    Output: Prints the selected quiz.
    """
    level = raw_input("Please select a difficulty: easy, medium, hard.  ").lower()
    if level.lower() == 'easy':
        print "You picked easy, good luck! "
        print easy_quiz
        return easy_quiz
    elif level.lower() == "medium":
        print "You picked medium, good luck!"
        print medium_quiz
        return medium_quiz
    elif level.lower() == "hard":
        print "You picked hard, good luck! "
        print hard_quiz
        return hard_quiz
    else:
        print "Invalid choice. Please enter easy, medium, or hard."
        choose_difficulty()

def answer_key(quiz):
    '''
    Behavior: Verifies the corresponding chosen answer key.
    Input: One of the three quizzes chosen.
    Output: Returns the corresponding answer key.
    '''
    if quiz == easy_quiz:
        return easy_answer
    if quiz == medium_quiz:
        return medium_answer
    if quiz == hard_quiz:
        return hard_answer

def game():
    '''
    Behavior: Initializes the game.
    Input: Prompts the player to enter number of desired tries and his/her answer to each blanks.
    Output: Whether the player answers correctly or incorrectly and if he/she wins or loses.
    '''
    quiz = choose_difficulty()
    answer = answer_key(quiz)
    blanks
    # allows the player to decide number of tries
    chances = int(raw_input("Before we begin, how many tries would you like to have? "))
    ans_num = 0
    while ans_num < len(blanks):
        player_answer = raw_input("What is the answer to" + blanks[ans_num] + "? ")
        if player_answer.lower() == answer[ans_num].lower():
            print "That is correct! "
            quiz = quiz.replace(blanks[ans_num], answer[ans_num])
            print quiz
            ans_num += 1
            if ans_num == len(blanks):
                print "Started from the bottom now we're here. You won!"
        else:
            chances -= 1
            wrong_ans(chances)

def wrong_ans(chances):
    '''
    Behavior: Verifies the chances when the player answers incorrectly.
    Input: The number of chances.
    Output: The remaining chances left or if there are none, ends the game.
    '''
    if chances > 0:
        print "Incorrect! Please try again. You have " + str(chances) + " chance(s) left. "
    elif chances == 0:
        print 'You lost and Drake is not happy. Thanks for playing!'
        raise SystemExit

game()
