import os
import whisper
import torch
import time
from datetime import timedelta
from pathlib import Path

def format_timestamp(seconds: float) -> str:
    """Convert seconds to HH:MM:SS format"""
    return str(timedelta(seconds=seconds)).split('.')[0]

def process_audio():
    print("Loading Whisper model...")
    # Choose model size based on your needs: tiny, base, small, medium, large-v3
    model = whisper.load_model("medium", device="cuda" if torch.cuda.is_available() else "cpu")
    
    input_path = Path("/app/input/audio.ogg")
    output_path = Path("/app/output/output.txt")
    
    print(f"Device being used: {'CUDA' if torch.cuda.is_available() else 'CPU'}")
    print("Starting transcription...")
    start_time = time.time()
    
    # Transcribe with word-level timestamps
    result = model.transcribe(
        str(input_path),
        language="ja",  # 日本語の場合
        word_timestamps=True,
        verbose=True
    )
    
    # Format output with timestamps
    with open(output_path, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            start = format_timestamp(segment["start"])
            text = segment["text"].strip()
            f.write(f"[{start}] {text}\n")
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Transcription completed in {duration:.2f} seconds")
    print(f"Output saved to: {output_path}")
    
    # Cleanup
    os.remove("/app/input/audio.ogg")

if __name__ == "__main__":
    process_audio()

# README.md
