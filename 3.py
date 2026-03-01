from datasets import load_dataset
import nemo.collections.asr as nemo_asr
import soundfile as sf

print("Loading dataset...")

# Disable automatic audio decoding
dataset = load_dataset(
    "ekacare/eka-medical-asr-evaluation-dataset",
    split="test",
    streaming=True
)

print("Loading model...")

model = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="QuartzNet15x5Base-En"
)

print("Starting transcription...")

for i, item in enumerate(dataset):
    if i == 3:   # only first 3 samples
        break

    audio_url = item["audio"]["path"]

    print("Processing:", audio_url)

    # save manually
    sf.write("temp.wav", item["audio"]["array"], 16000)

    result = model.transcribe(["temp.wav"])

    print("AI Output:", result[0].text)