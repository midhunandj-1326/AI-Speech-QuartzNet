import nemo.collections.asr as nemo_asr

print("Loading model...")

model = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="QuartzNet15x5Base-En"
)

print("Converting speech to text...")

text = model.transcribe(["sample.wav"])

print("Transcription Result:")
print(text[0].text)