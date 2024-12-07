import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(filename, duration, samplerate=44100):

    print(f"Recording for {duration} seconds...")
    # Record audio
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    print("Recording complete!")

    # Save the recorded audio to a WAV file
    write(filename, samplerate, audio_data)
    print(f"Audio saved to {filename}")


if __name__ == "__main__":
    print('Recording phone number....')
    # Specify the output filename, duration, and sampling rate
    output_file = "test1.wav"
    record_duration = 10  # seconds

    record_audio(output_file, record_duration)
