# AI-Speech-QuartzNet
Speech Recognition using QuartzNet
This project implements an Automatic Speech Recognition (ASR) system using the QuartzNet architecture and the NVIDIA NeMo framework. The objective of this project is to train a speech-to-text model capable of converting spoken audio into textual transcription using deep learning techniques.

---

## Project Overview

Automatic Speech Recognition (ASR) enables machines to understand and transcribe human speech. This project demonstrates a complete software-based pipeline for training an ASR model on a custom audio dataset.

The workflow includes:

- Audio dataset preparation
- Audio preprocessing
- WAV data organization
- Manifest file creation
- QuartzNet model training
- GPU-based deep learning workflow

---

## Model Architecture

QuartzNet is an end-to-end speech recognition neural network based on:

- 1D Time-Channel Separable Convolutions
- Connectionist Temporal Classification (CTC) Loss
- Deep convolutional acoustic modeling

Framework Used:
- NVIDIA NeMo ASR Toolkit
- PyTorch

---

## Dataset

Dataset Used: **UCLASS Processed for Machine Learning**

Dataset Characteristics:
- Preprocessed speech audio samples
- Corresponding transcription labels
- Suitable for supervised speech recognition training
- Organized for machine learning workflows

The dataset audio files were manually downloaded and prepared for training.

---
## Tech Stack

- Python 3.10
- PyTorch (CUDA Enabled)
- NVIDIA NeMo Toolkit
- QuartzNet ASR Model
- NVIDIA GPU (RTX Series)

---
### 1. Dataset Preparation
This step:
- Organizes downloaded audio files
- Generates WAV data structure
- Creates NeMo-compatible manifest file

---
### 2. Model Training
This step:
- Loads a pretrained QuartzNet model
- Fine-tunes using the prepared dataset
- Utilizes GPU acceleration for training

---

## Applications

- Speech-to-text systems
- Healthcare transcription
- Voice-controlled interfaces
- Assistive technologies
- Intelligent documentation systems

---

## Future Work

- Deployment using AMD Vitis AI acceleration workflow
- Model quantization and optimization for edge devices
- Real-time speech inference system
- Web-based speech recognition interface
- Edge AI deployment on embedded platforms

---
## License

MIT License — Free to use and modify.

---

## Acknowledgements

- NVIDIA NeMo Team
- PyTorch Community
- Open-source AI research community
