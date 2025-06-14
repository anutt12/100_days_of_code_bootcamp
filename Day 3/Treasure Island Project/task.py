from enum import Enum
from typing import Optional


class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"


class Action(Enum):
    SWIM = "swim"
    WAIT = "wait"


class DoorColor(Enum):
    RED = "red"
    YELLOW = "yellow"
    BLUE = "blue"


# ASCII Art Constants
TREASURE_MAP = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
INVALID_DOOR_ASCII = r'''             n     n
        n               n               n   n
     i                     n        i          n         n   n
   o                         n    o              n    i         n    i  n
 B                             g o                g o            g o      g
B                               B                  b              b        .

.'''

BEAST_ASCII = r'''                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
'''
FIRE_ASCII = r'''               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

TROUT_ASCII = r'''           .'|_.-
         .'  '  /_
      .-"    -.   '>
   .- -. -.    '. /    /|_
  .-.--.-.       ' >  /  /
 (o( o( o )       \_."  <
  '-'-''-'            ) <
(       _.-'-.   ._\.  _\
 '----"/--.__.-) _-  \|
AoS    "V""    "V"'''

HOLE_ASCII = r'''                                      +---+
                                      |\   \
  +-----------------------------+     | +---+
   \                      +-----------+ |   |
    \                      \            |   |
     \                 |/   +-----------+   |
      \                (c_      |   \ | |   |
       \                \       |    \| |   |
        \                       |     | |   |
         \                      |     + |   |
          \                     |      \| DM|
           \--------------------+       +---+
            \                    \        \
             \                    \        \
              +-----------------------------+'''

WIN_ASCII = r'''                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.   hjw'''


def display_game_over(message: str, ascii_art: str) -> None:
    """Display game over message with corresponding ASCII art."""
    print(f"{message} - Game Over.")
    print(ascii_art)


def choose_direction() -> Optional[Direction]:
    """Handle the first choice in the game."""
    choice = input("Would you like to go left or right? Type left or right: ").lower()
    return Direction(choice) if choice in [d.value for d in Direction] else None


def choose_action() -> Optional[Action]:
    """Handle the second choice in the game."""
    choice = input("Would you like to swim or wait? Type swim or wait: ").lower()
    return Action(choice) if choice in [a.value for a in Action] else None


def choose_door() -> Optional[DoorColor]:
    """Handle the door color choice."""
    prompt = ("You arrive at the island unharmed. There are three doors. One red, one yellow and one blue. "
              "Which colour do you choose? ")
    choice = input(prompt).lower()
    return DoorColor(choice) if choice in [d.value for d in DoorColor] else None


def play_single_game() -> bool:
    """Play a single game and return True to continue playing, False to quit."""
    print(TREASURE_MAP)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    # First choice
    direction = choose_direction()
    if direction == Direction.RIGHT:
        display_game_over("Fall into a hole", HOLE_ASCII)
        return ask_to_continue()

    # Second choice
    if direction == Direction.LEFT:
        action = choose_action()
        if action == Action.SWIM:
            display_game_over("Attacked by trout", TROUT_ASCII)
            return ask_to_continue()

        # Final choice
        if action == Action.WAIT:
            door_color = choose_door()
            if door_color == DoorColor.RED:
                display_game_over("It's a room full of fire", FIRE_ASCII)
                return ask_to_continue()
            elif door_color == DoorColor.YELLOW:
                print("You found the treasure. You Win!", WIN_ASCII)
                print(
                    "Congratulations! You've made it out of the island with treasure! "
                    "You've found the treasure and escaped from the island with treasure."
                )
                return ask_to_continue()
            elif door_color == DoorColor.BLUE:
                display_game_over("You enter a room of beasts", BEAST_ASCII)
                return ask_to_continue()
            else:
                display_game_over("You chose a door that doesn't exist", INVALID_DOOR_ASCII)
                return ask_to_continue()
    return ask_to_continue()


def ask_to_continue() -> bool:
    """Ask if a player wants to play again or quit."""
    while True:
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' for yes or 'n' for no.")


def play_game() -> None:
    """Main game loop."""
    while True:
        if not play_single_game():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
