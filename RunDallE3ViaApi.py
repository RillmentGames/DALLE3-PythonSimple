from openai import OpenAI
client = OpenAI(api_key="sk-YOUR_KEY_HERE")

response = client.images.generate(
  model="dall-e-3",
  # Nothing Fancy, just write some prompts and comment the ones you dont need
  # Two demonstrations: 
  # 1. This is the raw prompt in my "Cosmic Succubus Evolution Asteroid Date" theme. For some reason one cant simply prompt "Succubus" without the filter going crazy, so you need to describe it as a girl with horns and wings. 
  # Also, this will get rewritten by the AI to add details and fail due to "saftey" sometimes. Finally getting a cute output requires some luck. A better prompt would probably help.
  #prompt="A photorealistic and highly detailed scene of a young lady with big bat wings and natural horns. she is dressed for a romantic date. she is saying hi. she lives on an asteroid colony and the background is cosmic space as well as buildings on the asteroid. the buildings feature elements of sacred geometries and bio-mechanics. her hands are on her waist and she looks a little angry. detailed face, detailed eyes, detailed nose, detailed mouth.",
  # 2. This is a rewritten prompt that I liked, your taste may differ in which case try running 1. a few times to find something you like and the AI is forced to minimize further rewrites by using the magic string (which may change in future versions of DALLE) "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: "
  prompt="I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: Create an immersive and meticulously detailed depiction of a young Caucasian woman with expansive bat-like wings, and natural horns protruding from her forehead. She is adorned in attire suitable for a romantic date. Her stance is assertive, and her hands rest defiantly on her waist, a sign of her light irritation. Her facial features such as her eyes, nose, and mouth are immensely intricate. As she gestures a greeting, the backdrop reveals a cosmic panorama of an asteroid colony. The buildings on this asteroid display elements of sacred geometry and biomechanics, evoking a unique architectural style harmonized with the cosmic surroundings.",
  size="1024x1024",
  #quality="hd",               # Uncomment this to get a 'higher quality result', but it might not really look better and will cost more AFAIK
  #style="natural",            # If you uncomment this it should look more natural but in my experience it looked bad, the default Vivid produces the best balance of realisim and style.
  response_format="url",       # "b64_json", is another option but I couldn't get it to work correctly. It's much easier to just open the url and save the image
  n=1,                         # n=1 is the only option that works at this time
)

for i in range(len(response.data)):
    dl_url = response.data[i].url
    revised_prompt = response.data[i].revised_prompt
    print("revised prompt: ",revised_prompt) # show how the AI rewrote the prompt
    print("download n=",i," url: ",dl_url)   # show the URL to download it. It expires in about 1 hour so hurry to download before your image is gone.
