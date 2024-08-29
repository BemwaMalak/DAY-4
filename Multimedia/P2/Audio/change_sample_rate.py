from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_file("audiofile.wav")

# Convert the sample rate to 48 kHz
audio = audio.set_frame_rate(48000)

# Export the audio file
audio.export("example_audio_48kHz.wav", format="wav")