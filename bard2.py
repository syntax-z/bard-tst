import google.generativeai as palm
import os
import json
from pprint import pprint

PATH = os.path.dirname(os.path.realpath(__file__))
with open(PATH + "/config.json") as f:
    config = json.load(f)

palm.configure(api_key=config["token"])

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 250,
  'stop_sequences': []
}

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
        pprint(f"**CURRENT HISTORY**\n {chat_history}")
        continue

    response = palm.generate_text(
    **defaults,
    prompt=prompt
    )
    chat_history.append(f"input: {userinput}\n output: {response.result}")
    print(response.result)