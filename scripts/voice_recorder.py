# library for voice recording
import sounddevice

# library to write the recorded voice into a WAV file
from scipy.io.wavfile import write

#sample rate 
fs = 44100

#allow user to enter duration of recording in seconds
seconds = int(input("Enter recording duration in seconds: "))

print("Recoding....")

#let's do the recording
record_voice = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
#wait until recording is completed before proceeding
sounddevice.wait()

#write the recorded data into WAV file
write('recording.wav', fs, record_voice)

print('Recording completed')
