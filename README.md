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

## pre load model

comment in `docker-compose.yml` line 13
and `docker compose up` then into docker

```
# into docker
docker compose exec transcriber bash    
# download model
python3 -c "import whisper; whisper.load_model('medium')"
```

## wsl gpu setup

```
# NVIDIA-Container-Toolkitのインストール
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

```
# GPU認識の確認
nvidia-smi

# Dockerでのテスト
docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```

## sample

record video with obs and move to  `input` folder as `meeting.mp4`.  

[音声ファイルを聞く](./sample/audio.ogg)  

then,

```
[0:00:01] 政府をクレジットカードを持つ個人と考えてみるとわかりやすいぜ
[0:00:05] 終入
[0:00:06] わかりやすいのか?
[0:00:08] それはよくわからないけどな
```