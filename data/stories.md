## happy path 01
* greet
  - utter_main_menu
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "validmoviecode"}

## happy path 02
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidstart" : "validmoviecode"}

## sad path 01
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidstart" : "invalid"}
  - utter_wrong_movie_code

## sad path 02
* greet
  - utter_main_menu
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "invalid"}
  - utter_wrong_movie_code
