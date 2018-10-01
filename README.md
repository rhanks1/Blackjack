
# BLACKJACK

### To Play Game:
* Must have Python 3
* Need to install pydealer

If Python3 is installed and the default python language, run 
the following commands:
```pip install pydealer
python blackjack.py```

On many machines, Python2 is the default version eventhough Python3 is installed. 
If this is the case, run the following commands instead: 
```pip3 install pydealer```
```python3 blackjack.py```

To run unittests, run the following command in the top directory of the 
project:
```python3 -m unittest discover```

Rules for Blackjack: https://www.bicyclecards.com/how-to-play/blackjack/

Game Specifics:
* User will start with 100 chips
* Blackjack pays out 3:2
* Double Down and Split bets can be less than or equal to original bet
* Only one card will be dealt to Double Down and Split hands 
* No Insurance will be offered

Design Choices:
I wrote three classes to handle the core functionality of blackjack.
The Player and Dealer classes represent the player and dealer at the 
table, and the  GameManager class keeps track of what state the game 
is in and delegates tasks to the Player and Dealer in accordance with
blackjack protocol. Additionally, the GameManager handles all input from
the user and output to the console. 

The dictionary BJ_RANKS stores the value of the card and its point total 
for blackjack together. For example, BJ_RANKS["Queen"] == 10. 

The dictionary SUITS stores the string representation of suit and the 
unicode representation of suit together to improve the console display. 
For Example, SUITS['Hearts'] == '♥'.

The dictionary VALUES stores the string representation of face cards and
their one character representation together to improve console display.
For example, VALUES['King'] == 'K'. 

I used an external package "pydealer" for its Card, Stack, and Deck classes.
The Card class represents a playing card with a value and string pair, and 
it has some useful built in methods. The Stack class is a generic card 
container with built in methods to allow users to manipulate the cards held 
inside them. I used the Stack class to represent the player's and dealer's
hands. The Deck class is a subclass of Stack that has a few extra methods 
that you would expect decks to have. I used the Deck class to represent a 
deck of 52 playing cards.

Link to pydealer documentation: https://pydealer.readthedocs.io/en/latest/code.html

I decided to use python because it is objected oriented and easy to use for 
both developers and users. 

I decided to use unittest for all unittesting because it does not require the 
user to install any modules in order to use it. 
