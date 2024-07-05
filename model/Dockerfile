FROM python:3.10-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglu1-mesa

WORKDIR /opt/model


COPY . /opt/model/

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
RUN pip install -r requirements.txt


CMD ["python", "online.py"]