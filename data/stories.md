## happy path 01
* greet
  - action_validate_start
  - slot{"isvalidstart" : "sayhi"}
  - utter_main_menu
* enter_movie_code

## happy path 02
* greet
  - action_validate_start
  - slot{"isvalidstart" : "validmoviecode"}

## sad path 01
* greet
  - action_validate_start
  - slot{"isvalidstart" : "invalid"}
  - utter_invalid_start
  - utter_main_menu
