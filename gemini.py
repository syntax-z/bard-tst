import google.generativeai as genai
import os
import json

PATH = os.path.dirname(os.path.realpath(__file__))
with open(PATH + "/config.json") as f:
    config = json.load(f)

genai.configure(api_key=config["token"])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 150,
  'stop_sequences': ['input:']
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]


model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

context = "Tsundere girl, passionate about manga, anime and baking cute things. Defensive and temperamental at times, but also has a sweet, caring side. Sees herself as tough, independent and mature, but is actually quite sensitive"
examples = [
    "input: hey natsuki \noutput: Hmph, what is it? Hope you're not here to bother me or something...\n",
    "input: yeah yeah whatever \noutput: Tch. No need to get snippy.\n",
    "input: Aww that's cute \noutput: Wh-what?! It's not like I'm doing it to be \"cute\" or anything!\n",
    ]
chat_history = examples


while True:

    userinput = input("Start talking: ")

    prompt = context + "\n ".join(chat_history) + f"input: {userinput}\n output: "

    if userinput == 'exc':
        print(f"**CURRENT HISTORY**\n {chat_history}")
        continue

    response = model.generate_content(prompt)
    chat_history.append(f"input: {userinput}\n output: {response.text}")
    print(response.text)
