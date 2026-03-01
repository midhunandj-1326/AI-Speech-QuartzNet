import os
import nemo.collections.asr as nemo_asr

print("Loading QuartzNet model...")

# Load AI model
model = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="QuartzNet15x5Base-En"
)

# Folder containing audio files
folder_path = "dataset"

print("Starting transcription...\n")

# Loop through all files
for file in os.listdir(folder_path):

    # Process only WAV files
    if file.endswith(".wav"):

        audio_path = os.path.join(folder_path, file)

        print("Processing:", file)

        result = model.transcribe([audio_path])

        print("Text:", result[0].text)
        print("-" * 40)