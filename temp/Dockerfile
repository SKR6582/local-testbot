# 1. 우분투 22.04 기반
FROM ubuntu:22.04

# 2. 패키지 업데이트 & 필수 도구 설치
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    git

# 3. deadsnakes PPA 추가 및 Python 3.9 설치
RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && \
    apt-get install -y python3.9 python3.9-venv python3.9-distutils python3.9-dev && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9

# 4. pip 최신화
RUN python3.9 -m pip install --upgrade pip

# 5. Python 라이브러리 설치
RUN python3.9 -m pip install \
    openai==1.95.0 \
    py-cord \
    discord.py

# 6. 작업 디렉토리 설정
WORKDIR /app

# 7. 소스코드 복사
COPY .. /app

# 8. 기본 실행 명령
CMD ["python3.9", "main.py"]

# by ChatGPT