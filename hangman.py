
import time

game_word = "secret"

def hangman():
    name = raw_input("Your Name?\n")
    print "---Hello, " + name, "Time to play hangman!---"
    print "---OK! READY!!---"
    time.sleep(0.5)
    print "---Start guessing the word of 6 letters!!..."
    time.sleep(0.5)
    turns = 5 #total number to turn to guess
    print "---you have total", + turns, "chances!!--"

    
    guesses = ''
    wrong_guesses = ''
    #check if the turns are more than zero
    while turns > 0:         
        failed = 0               
        for char in game_word:      
            if char in guesses:    
                print char,    
            else:
                print "_",     
                failed += 1    
        if failed == 0:     # if failed is equal to zero   
            print "\n------YOU WON-----\n"  
            break  
        print 

        guess = raw_input("guess a character:") 
        guesses += guess 
         
        if guess not in game_word:
            wrong_guesses += guess
            count = len(wrong_guesses)
            #print wrong_guesses                   
            hangman_graphic(count)
                
            turns -= 1
                  
            print "---Guess letter is Wrong in game word---\n"    
            print "---You have", + turns, "more guesses!!---\n" 
            #print "maximum", +turns, "only!!\n"

            if turns == 0:           
                print "------GAME OVER!------"

def hangman_graphic(guesses):
        if guesses == 0:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /       "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|      "
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\    "
            print "|     /       "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|      0      "
            print "|     /|\     "
            print "|     / \     "
            print "|             "
            print "------GAME OVER!------"
            

hangman()