# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os
import json
from dotenv import load_dotenv
load_dotenv('.env.dev')

class ChatCompletion(object):
    chat_history = []
    def __init__(self, model_name = 'gpt-3.5-turbo'):
        super().__init__()
        self.model_name = model_name

    def get_chat_response(self, messages):

        res = ""

        self.chat_history.append(messages)  # add user message to chat history

        client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY")  # see .env
        )

        response = client.chat.completions.create(
            messages=self.chat_history,
            model = self.model_name,
            temperature=0.8,
            n=1,  # how many choices to get
            stream = True
        )

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                #print(type(chunk.choices[0].delta.content ))
                res += chunk.choices[0].delta.content or ""


        return res

## save time by streaming the response
## https://beta.openai.com/docs/guides/streaming/

#Typical chat completion using streaming
'''
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY")  # see .env
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",    # role: the role of the messenger (either system, user, assistant or tool)
            "content": "who are you",  # user messages
        },
    ],
    model="gpt-4",
    temperature=0.7,
    stream=True,
    n = 1  # how many choices to get
)
    
'''
### print ChatFormat
##print(json.dumps(json.loads(response.model_dump_json()), indent=4))



