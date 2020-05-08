import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import logging
logger = logging.getLogger(__name__)

class ActionValidateMovie(Action):
    def name(self):
        return "action_validate_movie"

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        moviecode_response = validateMovieCode(message)
        #logger.info(f'response here: {moviecode_response}')
        if moviecode_response is not None:
            validity = 'validmoviecode'
            movietitle = moviecode_response['data']['title']
            movieprice = moviecode_response['data']['price']
            image = moviecode_response['data']['image']
            dispatcher.utter_template('utter_movie_info', tracker, image_url=image, movietitle=movietitle, movieprice=movieprice)
        else:
            validity = 'invalid'

        return [SlotSet('isvalidmoviecode', validity), SlotSet('moviejson', moviecode_response)]

class ActionValidateSMC(Action):
    def name(self):
        return "action_validate_smc"
    
    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        smc_response = validateSmartcard(message)
        smcname = smc_response['data']['name']
        smcic = smc_response['data']['nric']
        if smc_response is not None:
            result = [SlotSet('isvalidsmc', 'validsmc'), SlotSet('smcnumber', message), SlotSet('smcname', smcname), SlotSet('smcic', smcic)]
        else:
            result = [SlotSet('isvalidsmc', 'invalid'), SlotSet('smcnumber', None), SlotSet('smcname', None), SlotSet('smcic', None)]
        
        return result

class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        #code here

        return []


class ActionValidateMenuOptions(Action):
    def name(self):
        return "action_validate_menu_options"

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        intent= tracker.latest_message['intent'].get('name')
        logger.info(f'intent here:{intent}')
        result = None
        if intent == 'menu_movie':
            if message == '00':
                result = [SlotSet('menuoptions', 'mainmenu')]
            elif message == '1':
                result = [SlotSet('menuoptions', 'smcmenu')]
        
        return result


# Validate movie code
def validateMovieCode(message):
    resp_json = None
    response = requests.get('http://a8525840.ngrok.io/api/njoi/movie/validate/{}'.format(message))
    if response.status_code == 200:
        resp_json = response.json()
    else:
        resp_json = None

    return resp_json

# Validate smartcard 
def validateSmartcard(message):
    resp_json = None
    response = requests.get('http://a8525840.ngrok.io/api/njoi/smc/validate/{}'.format(message))
    if response.status_code == 200:
        resp_json = response.json()
    else:
        resp_json = None

    return resp_json