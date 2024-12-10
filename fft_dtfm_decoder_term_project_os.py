import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, find_peaks

# DTMF frequency table of digits
dtmf_table = {
    (697, 1209): '1', (697, 1336): '2', (697, 1477): '3', (697, 1633): 'A',
    (770, 1209): '4', (770, 1336): '5', (770, 1477): '6', (770, 1633): 'B',
    (852, 1209): '7', (852, 1336): '8', (852, 1477): '9', (852, 1633): 'C',
    (941, 1209): '*', (941, 1336): '0', (941, 1477): '#', (941, 1633): 'D',
}

# Bandpass filter function
def bandpass_filter(_signal, low_cut, high_cut, _sampling_rate, order=6):
    nyquist = 0.5 * _sampling_rate
    low = low_cut / nyquist
    high = high_cut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, _signal)

# Find dominant frequencies in a spectrum
def find_dominant_frequencies(spectrum, frequencies, threshold=1.0):
    peaks, properties = find_peaks(spectrum, prominence=threshold)
    sorted_peaks = sorted(zip(frequencies[peaks], properties["prominences"]), key=lambda x: x[1], reverse=True)
    return [freq for freq, _ in sorted_peaks[:2]]

# Plot spectrogram
def plot_spectrogram(stft, sr, hop_length):


    plt.figure(figsize=(14, 6))
    librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max),
                             sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram of the Audio')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()

    # Frequency-Amplitude Graph
    fft_spectrum = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(fft_spectrum), d=1 / sampling_rate)
    amplitudes = np.abs(fft_spectrum)

    plt.figure(figsize=(14, 6))
    plt.plot(frequencies[:len(frequencies) // 2], amplitudes[:len(amplitudes) // 2])
    plt.title('Frequency-Amplitude Graph')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

# Main function
if __name__ == "__main__":
    print("Starting DTMF detection...")

    # Load audio
    audio_path = 'test1.wav'  # Replace with your file
    signal, sampling_rate = librosa.load(audio_path, sr=None)

    # Parameters
    frame_size = 2048
    hop_length = 512

    # filtering
    filtered_signal = bandpass_filter(signal, 650, 1700, sampling_rate)
    stft = np.abs(librosa.stft(filtered_signal, n_fft=frame_size, hop_length=hop_length))
    frequencies = librosa.fft_frequencies(sr=sampling_rate, n_fft=frame_size)

    # Analyze DTMF tones
    detected_tones = []
    time_segments = librosa.frames_to_time(range(stft.shape[1]), sr=sampling_rate, hop_length=hop_length)

    for frame_idx in range(stft.shape[1]):
        spectrum = stft[:, frame_idx]
        dominant_freqs = find_dominant_frequencies(spectrum, frequencies, threshold=10.0)

        if len(dominant_freqs) >= 2:
            dominant_freqs = tuple(sorted(dominant_freqs[:2]))
            for (row_freq, col_freq), number in dtmf_table.items():
                if abs(dominant_freqs[0] - row_freq) <= 15 and abs(dominant_freqs[1] - col_freq) <= 15:
                    detected_tones.append((time_segments[frame_idx], number))
                    break

    # Group tones into phone number
    phone_number = []
    debounce_threshold = 0.1  # Adjusted for realistic tone separation
    last_time = -float('inf')

    for time, tone in detected_tones:
        if time - last_time > debounce_threshold:
            phone_number.append(tone)
        last_time = time

    # Join detected tones into a single phone number
    final_number = ''.join(phone_number)

    # Display results
    print("Detected phone number:", final_number)

    # Plot spectrogram
    plot_spectrogram(stft, sampling_rate, hop_length)
