# Import necessary libraries
import gradio as gr
import librosa
import librosa.display
import numpy as np
import soundfile as sf
import tempfile
import os
import datetime

# Create input and output folders if they don't exist
input_folder = '/home/niket/Pictures/INPUT_VAD'
output_folder = '/home/niket/Pictures/OUTPUT_VAD'
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Define Voice Activity Detection (VAD) function using librosa
def vad_with_librosa(input_audio):
    
# Generate unique file name based on timestamp for input audio
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    temp_input_filename = f"input_{current_time}.wav"
    temp_input_path = os.path.join(input_folder, temp_input_filename)
    
# Write input audio data to temporary file in the input folder
    sf.write(temp_input_path, input_audio[1], samplerate=48000)

# Load input audio using librosa
    y, sr = librosa.load(temp_input_path, sr=16000)

# Apply voice activity detection (VAD)
    vad = librosa.effects.split(y, top_db=20)

# Get segments with voice activity
    segments = []
    for segment in vad:
        start = segment[0] * sr
        end = segment[1] * sr
        segments.append(y[start:end])

# Remove silent segment from the beginning of the audio file
    if len(segments) > 0:
        
# Calculate the duration of the first segment
        first_segment_duration = segments[0].shape[0] / sr

# Remove silent segment from the beginning
        segments[0] = segments[0][int(sr/2):]

# Remove silent segment from the end of the audio file
    if len(segments) > 1:
        
# Calculate the duration of the last segment
        last_segment_duration = segments[-1].shape[0] / sr

# Remove silent segment from the end
        segments[-1] = segments[-1][:int(-last_segment_duration*sr/2)]

# Concatenate segments
    output_audio = np.concatenate(segments)

# Pad or trim output audio to have a duration of 1 second
    desired_duration = sr  # 1 second
    if output_audio.shape[0] < desired_duration:
        
# Pad with zeros
        output_audio = np.pad(output_audio, (0, desired_duration - output_audio.shape[0]), mode='constant')
    else:
        
# Trim to desired duration
        output_audio = output_audio[:desired_duration]

# Convert output audio data to float32
    output_audio_data = output_audio.astype(np.float32)

# Generate unique file name based on timestamp for output audio
    temp_output_filename = f"output_{current_time}.wav"
    temp_output_path = os.path.join(output_folder, temp_output_filename)
    
# Write output audio data to temporary file in the output folder
    sf.write(temp_output_path, output_audio_data, samplerate=16000)

# Calculate duration of output audio in seconds
    duration = output_audio_data.shape[0] / sr
    
# Return the path to the output file and its duration    
    return temp_output_path, duration


# Define Gradio input and output components for the web interface
audio_input = gr.inputs.Audio(source="microphone", label="Input Audio")
audio_output = gr.outputs.Audio(type="numpy", label="Output Audio")
duration_output = gr.outputs.Label(label="Duration in seconds")


# Create and launch the Gradio interface
gr.Interface(
    vad_with_librosa,
    inputs=audio_input,
    outputs=[audio_output, duration_output],
    title="Voice Activity Detection").launch(server_port=6911)


# In[ ]:




