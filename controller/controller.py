import json

from model.OpenAiModel.chat_completion import ChatCompletion
from model.OpenAiModel.envVar import MODEL, CLIENT
from model.OpenAiModel.assistant import Assistant
from model.data.run_dynamic_data import update # do not remove
from openai import OpenAI
import googlemaps
from datetime import datetime
import os
client = CLIENT

class Controller:
    client = OpenAI()

    # Functions to get the static data from ../../data folder
    def get_static_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                print(data)
        except Exception as e:
            print(f"Error loading file {file_path}: {e}")
            return None

    # Functions to get the inputs from the website (api endpoint, get inputs as JSON)
    # Inputs are as such: {
    #    "Prompt": String
    #    "Max_Tokens": Number,
    #    "Temperature": Number,
    #    "Considerations": [String],
    # }

    # Functions to output the data to the website (POST to api endpoint, output as JSON)
    # Output is as such: {
    #    "response":
    #        {
    #            "text": String,
    #        }
    # }

    # Functions to get the real time data from ../model/data folder

    def get_ai_res(self, prompt):
        return ChatCompletion(MODEL).get_chat_response(prompt)

    def parse_input(self, input) -> str:
        """
        This function takes an input string and constructs a prompt for the AI model. 
        The prompt instructs the AI to parse the input and extract the starting and ending points 
        for a route that can be used in Google Maps. The output format is a JSON object with two keys, 
        'start' and 'end', and the values are the starting and ending points.

        Args:
            input (str): The input string to be parsed by the AI model.

        Returns:
            str: The AI model's response to the constructed prompt.
        """
        prompt = f"I am giving you an input. I want to you to read this input and get me the starting point and ending point "\
            f"such that I can simply plug it into Google maps and I can get a route from the starting point to the ending point. "\
            f"I want to the output format to be exactly like this: \n"\
            f"{{'start': 'starting point', 'end': 'ending point'}}. "\
            f"This is basically a JSON object with two keys, 'start' and 'end', and the values are the starting and ending points. "\
            f"Here is the input: \n"\
            f"{input}"
        return self.get_ai_res(prompt)

    def post_accident_bot_res(self, prompt):
        accident_description = prompt
        location = self.parse_input(prompt)
        loc = location if location else "Singapore"
        prompt = f"I am at this location: "
        prompt += loc + "\n"
        prompt += f"I just had an vehicular accident, "
        prompt += accident_description + "\n"
        prompt += f"please recommend me on the best medical advice"\
            f"and legal advice given my current situation"

        return self.get_ai_res(prompt)

    def greetings(self):
        greetings = f"Hello there! I'm TransportGPT, I have 3 versions of myself:\n"\
                f"1. I can help you with legal and medical advice using the latest data in a vehicular accident\n"\
                f"2. I can help you plan a route given your current start and end location given your preferences on ERP, weather conditions and eco-friendliness\n"\
                f"3. I can give you some route information to aide you in your travels.\n"
        return greetings
    
    async def get_real_time_data(self):
        apis = None
        with open("data/dynamic/apis.json", 'r') as file:
            apis = json.load(file)
        
        apiMock = {
            "interval": 10,
            "url": "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast",
            "name": "rainfall"
        }

        update(apiMock)
    

    def route_planner_res(self, prompt, choices):
        location = self.parse_input(prompt)
        return "POST ACCIDENT BOT"

    def route_info_res(self):
        return "POST ACCIDENT"
        
    def get_ai_res(self,prompt):
        return ChatCompletion().get_chat_response(prompt)

    def get_routes_from_input(self, start, end) :
        gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_CLOUD_API_KEY"))
        now = datetime.now()
        directions_result = gmaps.directions(start, end, mode="transit", departure_time=now)
        return directions_result
    
    def get_ai_res(self, prompt):


        my_assistants = client.beta.assistants.list(
            order="desc",
            limit="20",
        )

        print(my_assistants.data)




        run = client.beta.threads.runs.create(
        
        assistant_id = pricingAssistant.id
)

        #return pricingAssistant.get_assistant_response(prompt) + ""
    
    