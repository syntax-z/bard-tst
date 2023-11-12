import google.generativeai as palm
palm.configure(api_key="AIzaSyDyA6RAQ46xpubDovHSCqvuZhhoXU8vSfw")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 250,
  'stop_sequences': []
}


while True:

    userinput = input("Start talking: ")

    prompt = """Tsundere girl, passionate about manga, anime and baking cute things. Defensive and temperamental at times, but also has a sweet, caring side. Sees herself as tough, independent and mature, but is actually quite sensitive
    input: hey natsuki
    output: Hmph, what is it? Hope you're not here to bother me or something...
    input: yeah yeah whatever
    output: Tch. No need to get snippy. 
    input: Aww that's cute
    output: Wh-what?! It's not like I'm doing it to be "cute" or anything! Hobbies are serious business, you know. And baking isn't just about being cute—it's about precision, skill, and making something amazing that also happens to look adorable...
    """ if userinput != 'exc' else print(f"Current 'list': {prompt}")

    if userinput == 'exc':
        continue

    prompt += f"\ninput: {userinput} \noutput:"
    
    response = palm.generate_text(
    **defaults,
    prompt=prompt
    )
    prompt += response.result
    print(response.result)