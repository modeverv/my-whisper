#!/bin/bash
set -e

INPUT_FILE="/app/input/meeting.mp4"
AUDIO_FILE="/app/input/audio.ogg"
OUTPUT_FILE="/app/output/output.txt"

echo "Starting transcription process..."

# Extract and convert audio
echo "Converting audio..."
ffmpeg -i "$INPUT_FILE" \
    -vn \
    -acodec libopus \
    -ac 1 \
    -ar 16000 \
    -b:a 32k \
    "$AUDIO_FILE"

# Run transcription
echo "Running transcription..."
python3 ./src/transcribe.py

echo "Process complete!"

