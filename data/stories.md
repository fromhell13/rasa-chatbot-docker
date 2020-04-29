## happy path 01
* greet
  - action_validate_start
  - slot{"isvalidstart" : "sayhi"}
  - utter_main_menu
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "validmoviecode"}

## happy path 02
* greet
  - action_validate_start
  - slot{"isvalidstart" : "validmoviecode"}
  - action_validate_movie


## sad path 01
* greet
  - action_validate_start
  - slot{"isvalidstart" : "invalid"}
  - utter_invalid_start
  - utter_main_menu

## sad path 02
* greet
  - action_validate_start
  - slot{"isvalidstart" : "sayhi"}
  - utter_main_menu
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "invalid"}
