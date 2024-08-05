<div align="center">

<h1>RVC Inference</h1>

<div>
	<mark>Make sure to create new conda environment with python 3.10</mark> <br>
</div>

```bash
python --version # 3.10
```

### 手动安装依赖
1. 安装`pytorch`及其核心依赖，若已安装则跳过。参考自: https://pytorch.org/get-started/locally/
```bash
pip install torch torchvision torchaudio
```

3. 根据自己的显卡安装对应依赖
- N卡
```bash
pip install -r requirements.txt
```

## Download the Models

Follow these steps to download and install the models:

1. Download the `.deb` package:
```bash
wget https://github.com/RVC-Project/RVC-Models-Downloader/releases/download/v0.2.2/rvcmd_linux_amd64.deb
```

2. Install the downloaded package:
```bash
sudo apt install ./rvcmd_linux_amd64.deb
```

3. Run the command to download all assets:
```bash
rvcmd -notrs -w 1 -notui assets/all
```



### 2. 安装 ffmpeg 工具
若已安装`ffmpeg`和`ffprobe`则可跳过此步骤。

#### Ubuntu/Debian 用户
```bash
sudo apt install ffmpeg
``

## 开始使用
### 直接启动
使用以下指令来启动 WebUI
```bash
python rvc_infer.py
```

## 参考项目
+ [ContentVec](https://github.com/auspicious3000/contentvec/)
+ [VITS](https://github.com/jaywalnut310/vits)
+ [HIFIGAN](https://github.com/jik876/hifi-gan)
+ [Gradio](https://github.com/gradio-app/gradio)
+ [FFmpeg](https://github.com/FFmpeg/FFmpeg)
+ [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui)
+ [audio-slicer](https://github.com/openvpi/audio-slicer)
+ [Vocal pitch extraction:RMVPE](https://github.com/Dream-High/RMVPE)
  + The pretrained model is trained and tested by [yxlllc](https://github.com/yxlllc/RMVPE) and [RVC-Boss](https://github.com/RVC-Boss).

## 感谢所有贡献者作出的努力
<a href="https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/graphs/contributors" target="_blank">
  <img src="https://contrib.rocks/image?repo=RVC-Project/Retrieval-based-Voice-Conversion-WebUI" />
</a>
