import numpy as np
import soundfile as sf

# Parameters
sample_rate = 44100  # Sample rate in Hz
duration = 2.0       # Duration in seconds
frequency = 440.0    # Frequency of the sine wave in Hz (A4 note)

# Generate time values
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate sine wave
audio_signal = 0.5 * np.sin(2 * np.pi * frequency * t)

# Save the audio signal to a file
sf.write('sine_wave.wav', audio_signal, sample_rate)