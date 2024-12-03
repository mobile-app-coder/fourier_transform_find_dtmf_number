DTMF Tone Decoder
A Python-based program for decoding Dual-Tone Multi-Frequency (DTMF) signals from audio files. This project extracts keypad presses from DTMF tones commonly used in telecommunication systems, such as telephone keypads, and visualizes the results.

Features
🎵 Decode DTMF tones from audio signals.
🔢 Identify pressed keys and group them into phone numbers.
📊 Plot spectrograms and frequency-amplitude graphs for detailed signal analysis.
🚀 Robust frequency detection with adaptive debouncing and grouping.

Technologies Used
Python 3.x: Programming language.
Librosa: For audio signal processing.
NumPy: For numerical operations.
Matplotlib: For plotting and visualization.
SciPy: For signal filtering and peak detection.

Setup and Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/your_username/dtmf-tone-decoder.git
cd dtmf-tone-decoder

3. Install Dependencies
Install the required Python libraries using pip:

bash
Copy code
pip install -r requirements.txt
Create a requirements.txt file with the following content:

Copy code
librosa
numpy
matplotlib
scipy

3. Add Your Audio File
Place your .wav audio file containing DTMF tones in the project directory.
Update the audio_path variable in the code with your file name:

python
Copy code
audio_path = 'your_audio_file.wav'
Usage
Run the Program
bash
Copy code
python dtmf_decoder.py
Output
Terminal Output:
Displays the detected phone numbers.

plaintext
Copy code
Detected phone number(s):
1234567890
Visualization:
Generates a spectrogram and a frequency-amplitude graph.
Example spectrogram:


Code Overview
Main Steps:
Load the Audio: Load the .wav file and process the audio signal.
Filter and Transform: Use STFT to analyze the signal in the time-frequency domain.
Detect Frequencies: Identify dominant frequencies in each frame and match them with DTMF frequencies.
Group Detected Tones: Group detected tones into phone numbers based on timing.
Visualize: Plot spectrograms and frequency spectrum graphs.
How It Works
DTMF Basics
Each DTMF tone consists of two simultaneous frequencies:

Row Frequencies (Hz)
Column Frequencies (Hz)
Row Frequencies (Hz)	Column Frequencies (Hz)
697	1209
770	1336
852	1477
941	1633
Examples:

Pressing "1" generates 697 Hz and 1209 Hz.
Pressing "5" generates 770 Hz and 1336 Hz.
Frequency Detection
The program identifies the most prominent frequencies in each frame using peak detection.

Matching
Detected frequencies are matched with the predefined DTMF table.

Debouncing and Grouping
Removes duplicates and groups tones into phone numbers based on timing.

Contributing
Contributions are welcome! Here’s how you can help:

Fork the repository.
Create a new branch (feature/some-feature).
Commit your changes.
Push to the branch.
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or feedback, please contact:

Shahriyor: shahriyorturayev4@gmail.com
GitHub Profile: https://github.com/mobile-app-code
Notes:
Links: Replace [https://github.com/your_username/dtmf-tone-decoder.git](https://github.com/mobile-app-coder/fourier_transform_find_dtmf_number) with your actual repository link.
Images: Add your spectrogram image (e.g., example_spectrogram.png) to the repository to display it properly.
