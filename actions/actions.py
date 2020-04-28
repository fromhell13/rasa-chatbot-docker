import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import logging
logger = logging.getLogger(__name__)


class ActionJoke(Action):
  def name(self):
    return "action_joke"

  def run(self, dispatcher, tracker, domain):
    request = requests.get('http://api.icndb.com/jokes/random').json()  # make an api call
    joke = request['value']['joke']  # extract a joke from returned json response
    dispatcher.utter_message(text=joke)  # send the message back to the user
    return []

class ActionValidateStart(Action):
  def name(self):
    return "action_validate_start"

  def run(self, dispatcher, tracker, domain):
    return [SlotSet('isvalidstart', 'validmoviecode')]