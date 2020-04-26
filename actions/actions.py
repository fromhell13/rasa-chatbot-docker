
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionJoke(Action):
  def name(self) -> Text:
    return "action_joke"

  def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    request = requests.get('http://api.icndb.com/jokes/random').json()  # make an api call
    joke = request['value']['joke']  # extract a joke from returned json response
    dispatcher.utter_message(text=joke)  # send the message back to the user
    return []
