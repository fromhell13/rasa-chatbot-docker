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
    validity = None

    if message.lower() == 'hi':
        validity = 'sayhi'
    else:
        moviecode_response = validateMovieCode(message)
        if moviecode_response is not None:
            validity = 'validmoviecode'
        else:
            validity = 'invalid'
    
    return [SlotSet('isvalidstart', validity), SlotSet('moviejson', moviecode_response)]

class ActionValidateMovie(Action):
    def name(self):
        return "action_validate_movie"
        
    def run(self, dispatcher, tracker, domain):
        movies = tracker.get_slot('moviejson')
        validity, moviecode_response = None, None
        if movies is not None:
            movietitle = movies['data']['title']
            movieprice = movies['data']['price']
            image = movies['data']['image']
            dispatcher.utter_template('utter_movie_info', tracker, image_url=image, movietitle=movietitle)
        else:
            message = tracker.latest_message.get('text')
            moviecode_response = validateMovieCode(message)
            if moviecode_response is not None:
                validity = 'validmoviecode'
                movietitle = moviecode_response['data']['title']
                movieprice = moviecode_response['data']['price']
                image = moviecode_response['data']['image']
                dispatcher.utter_template('utter_movie_info', tracker, image_url=image, movietitle=movietitle)
            else:
                validity = 'invalid'

        return [SlotSet('isvalidmoviecode', validity), SlotSet('moviejson', moviecode_response)]

# Validate movie code
def validateMovieCode(message):
    resp_json = None
    response = requests.get('http://a8525840.ngrok.io/api/movies/validate/{}'.format(message))
    if response.status_code == 200:
        resp_json = response.json()
    else:
        resp_json = None

    return resp_json