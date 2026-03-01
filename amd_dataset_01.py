from datasets import load_dataset, Audio
import os
import soundfile as sf
import json

print("Loading dataset...")

# LOAD DATASET WITHOUT TORCHCODEC
dataset = load_dataset(
    "ekacare/eka-medical-asr-evaluation-dataset",
    "en",
    split="test"
)

# IMPORTANT ⭐ Disable automatic decoding
dataset = dataset.cast_column("audio", Audio(decode=False))

print("Dataset loaded:", len(dataset))

# Create folders
os.makedirs("quartz_dataset/wavs", exist_ok=True)

manifest_path = "quartz_dataset/manifest.json"

print("Converting audio...")

with open(manifest_path, "w") as manifest:

    for i, sample in enumerate(dataset):

        audio_info = sample["audio"]

        # Read raw audio bytes manually
        audio_bytes = audio_info["bytes"]

        wav_path = f"quartz_dataset/wavs/sample_{i}.wav"

        # Save wav manually
        with open(wav_path, "wb") as f:
            f.write(audio_bytes)

        entry = {
            "audio_filepath": os.path.abspath(wav_path),
            "text": sample["text"],
            "duration": sample["duration"]
        }

        manifest.write(json.dumps(entry) + "\n")

        if i % 500 == 0:
            print(f"Processed {i}")

print("✅ DONE — Dataset ready for training!")