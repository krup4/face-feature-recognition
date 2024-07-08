FROM python:3.10-slim AS builder

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglu1-mesa libglib2.0-0

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio
#--index-url https://download.pytorch.org/whl/cu121
RUN pip install -r requirements.txt


FROM builder as runtime

WORKDIR /opt/model

COPY . .

RUN python download_weights.py

CMD ["python", "analysis_frame.py"]