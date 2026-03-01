import json
import nemo.collections.asr as nemo_asr

print("Loading QuartzNet model...")

# Load AI model
model = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="QuartzNet15x5Base-En"
)

# Load dataset file
with open("dataset_info.json", "r") as f:
    data = json.load(f)

print("Starting transcription...")

for item in data:
    audio_path = item["audio_filepath"]

    print(f"\nProcessing: {audio_path}")

    result = model.transcribe([audio_path])

    print("AI Output:", result[0].text)