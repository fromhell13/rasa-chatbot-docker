## happy path 01
* greet
  - utter_main_menu
  - utter_test_response
* enter_movie_code
  - action_validate_movie
  - slot{"isvalidmoviecode" : "validmoviecode"}
* menu_movie
  - action_validate_menu_options
  - slot{"menuoptions":"smcmenu"}
  - utter_ask_smartcard
* key_in_smartcard
  - action_validate_smc
  - slot{"isvalidsmc":"validsmc"}
  - utter_purchase_summary

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

## back to main menu
* menu_movie
  - action_validate_menu_options
  - slot{"menuoptions":"mainmenu"}
  - utter_main_menu

## Enter SmartCard
* enter_smartcard
  - utter_ask_smartcard

## invalid smc
* key_in_smartcard
  - action_validate_smc
  - slot{"isvalidsmc":"invalid"}
  - utter_invalid_smc
