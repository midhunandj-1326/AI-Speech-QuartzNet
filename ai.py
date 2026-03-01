import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000          # audio quality (standard for speech AI)
seconds = 30        # recording time = 30 seconds

print("Speak now... Recording for 30 seconds")

audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()   # wait until recording finishes

write("sample.wav", fs, audio)

print("Recording saved as sample.wav")