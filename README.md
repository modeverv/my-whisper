# Whisper Local Transcription

## Setup
1. Install Docker and NVIDIA Container Toolkit
2. Place your OBS recording (mp4) in the `input` folder as `meeting.mp4`
3. Run: `docker-compose up --build`

## Configuration Options:
- Edit `src/transcribe.py` to change Whisper model size:
  - tiny: 速い、低精度
  - base: バランス
  - small: 良好な精度
  - medium: 高精度
  - large-v3: 最高精度、低速