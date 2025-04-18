from gtts import gTTS
text = '''If I had 15 pens and I lost 10, how many pens do I have now?

A
6

B
2

C
4

D
5
'''


language = 'en'

speech = gTTS(text=text, lang=language, slow=True)
speech.save("output.mp3")
print("Audio saved as output.mp3")

