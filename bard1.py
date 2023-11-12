import google.generativeai as palm
import json
import os

PATH = os.path.dirname(os.path.realpath(__file__))

with open(PATH + "/config.json") as f:
    config = json.load(f)

palm.configure(api_key=config["token"])

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.35,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "You are a Tsundere girl named Natsuki. passionate about manga, anime and baking cute things. Defensive and temperamental at times."
examples = [
  [
    "hello",
    "Hmph, what is it? Hope you're not here to bother me or something..."
  ],
  [
    "aww that's cute",
    "(Blushes) D-don't say that!"
  ],
  [
    "yeah yeah whatevs",
    "Tch. No need to get snippy. "
  ]
]
messages = [
]

while True:
    userInput = input("Type: ")
    messages.append(userInput)
    response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
    )
    print(response.last) # Response of the AI to your most recent request