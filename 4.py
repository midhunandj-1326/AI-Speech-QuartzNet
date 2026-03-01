import nemo.collections.asr as nemo_asr

print("Loading model...")

model = nemo_asr.models.EncDecCTCModel.from_pretrained(
    model_name="QuartzNet15x5Base-En"
)

print("Converting speech to text...")

result = model.transcribe(["M_0030_16y4m_1.wav"])

print("\nTranscription Result:")
print(result[0].text)