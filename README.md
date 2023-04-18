` `**README**

# **1. PROJECT NAME:**
- Creating a Gradio interface where input is Microphone for recording audio and output is VAD applied audio of 1 second.

**2. PROJECT OVERVIEW:**

- This code implements a Voice Activity Detection (VAD) system using Librosa, a popular Python library for audio analysis.
- The VAD system which is hosted on a Gradio interface takes an input audio from the microphone as a source and detects segments with voice activity in the audio.
- The detected segments are then saved as an output audio file with the silent segments removed from the beginning and end, and the output audio is padded or trimmed to 1 second and given as an output in Gradio.

**3.** **DEPENDENCIES:**

- gradio
- librosa
- numpy
- soundfile
- tempfile
- os
- datetime

**4. WORKING:**

- The input audio is recorded from the microphone using the Gradio library.
- The input audio data is saved as a temporary file in the input folder with a unique filename based on the timestamp.
- The input audio is loaded using Librosa and resampled to a sample rate of 16000 Hz.
- Voice activity detection is applied to the input audio using Librosa's effects.split function, which detects segments with voice activity based on a threshold of 200 dB.
- The segments with voice activity are extracted from the input audio and saved as temporary files in the output folder.
- Silent segments from the beginning and end of the audio are removed by trimming the segments.
- The segments are concatenated to create the output audio.
- If the duration of the output audio is less than 1 second, it is padded with zeros. If it is longer, it is trimmed to 1 second.
- The output audio data is saved as a temporary file in the output folder with a unique filename based on the timestamp.
- The path of the output audio file and its duration in seconds are returned as outputs to the Gradio interface.
- The Gradio interface displays the output audio and duration to the user.

**5. LICENSE:**

- This project is licensed under the MIT LICENSE.

**6.** **CONTACT INFORMATION:**

- For any questions or feedback, please contact:

Name- Niket Virendra Patil

Email- pniket7@gmail.com



