print('''
      0
   . \ /  _    +     .  ______   .          .
 (      /|\      .    |      \      .   +
     . |||||     _    | |   | | ||         .
.      |||||    | |  _| | | | |_||    .
   /\  ||||| .  | | |   | |      |       .
__||||_|||||____| |_|_____________\__________
. |||| |||||  /\   _____      _____  .   .
  |||| ||||| ||||   .   .  .         ________
 . \|`-'|||| ||||    __________       .    .
    \__ |||| ||||      .          .     .
 __    ||||`-'|||  .       .    __________
.    . |||| ___/  ___________             .
   . _ ||||| . _               .   _________
_   ___|||||__  _ \\--//    .          _
     _ `---'    .)=\oo|=(.   _   .   .   __
_  ^      .  -    . \.|.................|  |
''')

print("Welcome to Wonder Desert Island")
print("Your mission is to Exit the island before time runs out")

print("Note wrong input ends the game and you loss")

choice1 = input('Would you like to "Play" or "Exit"? ').lower()
if choice1 == "play":
    choice2 = input('You are at a bridg would you like to "Cross" or "Wait"? \n').lower()
    if choice2 == "cross":
        choice3 = input('You are at the top of the giant tactics would you like to "Jump" or "Wait"? \n').lower()
        if choice3 == "wait":
            choice4 = input('You were lucky to move to the floating house, Do you want to "Stay" or "Move"? \n').lower()
            if choice4 == "move":
                choice5 = input('You are at the base of the house would you like to go "Under" or "Back"? \n').lower()
                if choice5 == "under":
                    choice6 = input('You are at an underground tunnel and you heard a sound would you want to "Wait" or "Run"? \n').lower()
                    if choice6 == "wait":
                        choice7 = input('Good choice! You have found a human guide to help you out of the tunnel and the gate is ahead, then he tells you to wait \n At this point you are thirsty and there is a stream of water to your left but your time is almost up \n Would you move "Left" or "Wait" or "Run" towards the gate? \n').lower()
                        if choice7 == "wait":
                            print('He gave you water and shoes that make you run faster, You WIN Sorry I doubted, you were born to conquer!')
                        elif choice7 == "run":
                            print('You run towards the gate but began to hallucinate and died from thirst, You loss. I told you to quit while you had dignity.')
                        elif choice7 == "left":
                            print('You picked left and ran towards the stream, but it looks like you were hallucinating from the heat \n and there was nothing there You loss and dead from thirst and time up. \n At this point its just sad to watch you loss.')
                        else:
                            print('You seriously need help cause you didn\'t even type the right choice')
                    else:
                        print('You run and hit a dead end filled with snakes, You loss you should just give up, we are not all made to win.')
                else:
                    print('Going back into the house built pressure and you fell, You loss maybe you are just not a winner.')
            else:
                print('The pressure of you staying in the house for too long collapsed the house, You loss')
        else:
            print('It looks like you fell to the ground, Ooops you dead.')
    else:
        print('Ooops you were killed by falling rocks You loss')
else:
    print("You stopped before the adventure began...")