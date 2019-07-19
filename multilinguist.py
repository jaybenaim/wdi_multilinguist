import requests
import json
import random
class Multilinguist:
  """This class represents a world traveller who knows 
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'
    
    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool 
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    return json_response['translationText']


class MathGenius(Multilinguist): 
  def __init__(self): 
    super().__init__()
    
  def report_total(self, list_of_numbers): 
    sum_numbers = 0 
    for number in list_of_numbers: 
      sum_numbers += number 
    message = f'The sum of the numbers from the list is {sum_numbers} '
    
    
    return self.say_in_local_language(message)

class QuoteCollector(Multilinguist): 
  
  def __init__(self): 
    super().__init__() 
    self.fav_quotes = ["The foolish man think with narrow mind and speak with wide mouth.-Charlie Chin", "Seek the truth, no matter where it lies.-Metallica", "The strength of the Constitution lies entirely in the determination of each citizen to defend it.-Albert Einstein", "Conservatives want live babies so they can raise them to be dead soldiers.-George Carlin", "Conservatives want live babies so they can raise them to be dead soldiers.-George Carlin", "We've got far too many hung juries and not enough hung defendants.-Dennis Miller", "There is no knowledge that is not power.-Mortal Kombat 3"] 
    self.quote_with_topic = []

  def add_quote(self, quote, topic):
    # topics = {} 
    # topics[quote] = topic
    self.fav_quotes.append(quote) 
    self.quote_with_topic.append(topic)
  
  def random_quote(self): 
    quote = random.choice(self.fav_quotes) 
    return self.say_in_local_language(quote)
    
  
    

# me = MathGenius()
# print(me.report_total([23,45,676,34,5778,4,23,5465])) # The total is 12048
# me.travel_to("France")
# print(me.report_total([6,3,6,68,455,4,467,57,4,534])) # है को कुल 1604
# me.travel_to("Italy")
# print(me.report_total([324,245,6,343647,686545])) # È Il totale 1030767


quoter = QuoteCollector()
print(quoter.random_quote())
quoter.travel_to("France")
print(quoter.random_quote())
quoter.travel_to("Italy")
quoter.add_quote('hello', 'random')
print(quoter.random_quote())


