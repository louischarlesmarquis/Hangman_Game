import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['abruptly', 'absurd', 'abyss', 'affix','alpha', 'askew','ashtray','asshat', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo','banter', 'bayou', 'beekeeper',
             'bikini', 'blitz', 'blizzard','boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb','clench',
             'cockiness','colonoscopy', 'croquet','crotch', 'crypt','cum','curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus',
             'faking','fat','fart', 'fishhook', 'fixable','fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize',
             'gazebo', 'giaour', 'gizmo','glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy',
             'jackpot', 'jaundice','jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox',
             'jumbo', 'kayak','kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack','larvae', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph','mansplaining','materialgwrl', 'marquis', 'matrix', 'megahertz',
             'mango','microwave', 'mnemonic','minecraft', 'mystify','naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph','orange', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel',
             'parnell','penis','pizazz', 'pneumonia','Pneumonoultramicroscopicsilicovolcanoconiosis','proctology','polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb','rhythm',
             'rickshaw','scalar','schnapps', 'scratch','shark', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway','Supercalifragilisticexpialidocious', 'swivel',
             'syndrome','thief', 'thriftless', 'thumbscrew','toe', 'topaz','toz','transcript', 'transgress', 'transplant', 'triphthong','troubadour','turtle', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown',
             'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex','voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy','whiskey','whizzing', 'whomever','whore','wifey', 'wimpy',
             'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper',
             'zoboomafoo','zodiac', 'zombie', ]


print( ''' Welcome to my hangman game in python ''')

play_again=True

while play_again:
    
    chosen_word=random.choice(word_list)
    word_length=len(chosen_word)
    count=0
    final_word=[]
    alr_chosen=[]
    while(count<word_length):
        final_word.append("_")
        count+=1
    #Can use a for loop
    #for n in chosen_word:
    #    final_word.append("_")

    is_done=False
    has_won=False
    lives=6

    while not is_done:
        #join all elements of list together and print on screen
        print(f"{' '.join(final_word)}")
        
        guess = input("Guess a letter: ").lower()

        count=0
        
        if guess in alr_chosen:
            print(f"You have already chose the letter {guess}")
        else:
            if guess not in chosen_word:
                lives-=1
                print("Lmao")
                print(stages[lives])
            else:
            #Can use range
            #for position in range(word_length):
                for letter in chosen_word:
                    if letter == guess:
                        final_word[count]=guess
                    count+=1

        alr_chosen.append(guess)
        print()

        if "_" not in final_word:
            has_won=True
            is_done=True
            print("You win!")
            
        if lives==0:
            is_done=True
            print("LOSERRRRR")
            print(f"The word was {chosen_word}")

    user_input=input("Would you like to play again?(Y/N)").upper()
    if user_input=="Y":
        continue
    else:
        # nw play_again==False
        break
    
 
print("Thank you for playing my game:)")
