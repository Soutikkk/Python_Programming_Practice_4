from gtts import gTTS

# Read text file
with open("book.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Convert text to speech
audio = gTTS(text=text, lang="en")

# Save audiobook
audio.save("audiobook.mp3")

print("Audiobook created: audiobook.mp3")