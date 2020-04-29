import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import logging
logger = logging.getLogger(__name__)



class ActionValidateStart(Action):
  def name(self):
    return "action_validate_start"

  def run(self, dispatcher, tracker, domain):
    message = tracker.latest_message.get('text')
    returnSlot = None

    if message.lower() == 'hi':
        returnSlot = 'sayhi'
    else:
        validity = validateMovieCode(message)
        if validity:
            returnSlot = 'validmoviecode'
        else:
            returnSlot = 'invalid'
    return [SlotSet('isvalidstart', returnSlot)]

def validateMovieCode(message):
    valid = False
    response = requests.get('http://localhost:3000/api/movies/validate/{}'.format(message))
    if response.status_code == 200:
        resp_json = response.json()
        movietitle = resp_json['data'][0]['title']
        movieprice = resp_json['data'][0]['price']
        image = resp_json['data'][0]['image']
        SlotSet('movietitle', movietitle), SlotSet('movieprice',movieprice), SlotSet('image', image)
        valid = True
    else:
        SlotSet('movietitle', None), SlotSet('movieprice',None), SlotSet('image', None)
        valid = False

    return valid