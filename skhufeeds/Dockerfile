FROM python:3-alpine

# 앱 디렉터리 생성
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# 서버측 소스코드 복사
COPY . /usr/src/app

# 의존성 설치 - Python 모듈 패키지
RUN apk add --no-cache mariadb-client && pip install -r requirements.txt

# 3000 번 포트 노출
EXPOSE 3000

# 실행 명령
CMD python3 manage.py runserver 0.0.0.0:3000
