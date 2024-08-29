import soundfile as sf

# Read the audio file
data, sample_rate = sf.read('audiofile.mp3')

# Get the bit depth from the data type
bit_depth = data.dtype

# Determine the number of channels
channels = data.shape[1] if len(data.shape) > 1 else 1

print(f'Sample Rate: {sample_rate} Hz')
print(f'Bit Depth: {bit_depth}')
print(f'Channels: {channels}')