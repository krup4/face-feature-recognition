FROM python:3.10-slim AS builder

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglu1-mesa libglib2.0-0
RUN apt-get install -y curl

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio
#--index-url https://download.pytorch.org/whl/cu121
RUN pip install -r requirements.txt


FROM builder as runtime

WORKDIR /opt/model

COPY . /opt/model/

RUN chmod +x /opt/model/download_weights.sh
RUN /bin/bash /opt/model/download_weights.sh

CMD ["python", "analysis_frame.py"]