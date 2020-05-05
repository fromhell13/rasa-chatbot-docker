## happy path 01
* greet
  - utter_main_menu
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "validmoviecode"}
* enter_smartcard
  - utter_ask_smartcard

## happy path 02
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "validmoviecode"}

## sad path 01
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "invalid"}
  - utter_wrong_movie_code

## sad path 02
* greet
  - utter_main_menu
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "invalid"}
  - utter_wrong_movie_code

## happy path but with back to main menu
* greet
  - utter_main_menu
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "validmoviecode"}
* back_mainmenu
  - utter_main_menu
