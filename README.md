# Game_Center
School project from Alex and Diego.

Pseudocode:

// Initialize game

Player makes a chip bet of up to 100 chips
Create deck of cards
Shuffle deck
Deal two cards to player and two cards to dealer
// Start game loop

Display player and dealer's current hand
Ask player if they want to hit or stand
If player hits, deal another card to player's hand
If player's hand value is over 21, player busts and game ends
If player stands, dealer's turn begins
If dealer's hand value is less than 18, dealer hits
If dealer's hand value is over 21, dealer busts and game ends
If dealer's hand is 18 or higher, compare player and dealer's hand values
If player has higher hand value, player wins
Add winnings and initial bet back to player chipcount
If dealer has higher hand value, dealer wins
Subtract bet from player chipcount
If hand values are equal, game is a tie
Player keeps current chipcount no chips added or lost
// End game

Ask if player wants to play again
If yes, start new game
If no, end program