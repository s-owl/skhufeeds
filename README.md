# SKHUFEEDS

카카오톡 플러스친구 자동응답API 를 이용한 교내 소식 전달 시스템.

## 의존성

- Python 3.*
- MySQL
- RabbitMQ

- Python 모듈
 - Django >= 1.11.3
 - python-jose >= 1.4.0
 - mysqlclient >= 1.3.12
 - celery >= 4.1.0
 - beautifulsoup4 >= 4.6.0
 - pyshorteners >= 0.6.1
 - gunicorn >= 19.7.1
 - pyexcel-xls >= 0.5.0

## 플러스친구 계정 설정

- 카카오톡 플러스친구 관리자 페이지(https://center-pf.kakao.com/login) 에서 로그인 합니다.
- SKHUFEEDS 서버와 연결할 플러스친구 계정을 선택하거나, 새로 생성합니다.
- 좌측 매뉴에서, 스마트채팅을 선택하고. 이후 API형의 편집 버튼을 누릅니다.
- 서버 배포 작업을 먼저 합니다.
- 앱 이름, 앱 URL(서버에 배포되어 실행중인 앱이 가지는 URL), 설명 등을 입력합니다.
- API 테스트 버튼을 눌러 작동 여부를 확인합니다.
- API 형 저장하기를 눌러 설정을 저장합니다.
- 스마트채팅 선택 화면에서, API 형 편집 버튼 옆의 시작하기 버튼을 눌러 활성화 합니다.

## 서버 배포 작업

- MySQL Shell 에 `root` 로 접속하여, 데이터베이스를 새로 생성합니다.

```
 CREATE USER username@localhost IDENTIFIED BY 'password';
 CREATE DATABASE skhufeedsdb CHARACTER SET UTF8;
 GRANT ALL PRIVILEGES ON skhufeeds.* TO username@localhost;
 FLUSH PRIVILEGES;
 exit
```

명령행 셸 세션에서 아래와 같이 실행에 필요한 환경 변수를 설정합니다.

```
export SECRET_KEY = "(DJANGO SECRET_KEY : 암호화 등에 사용되는 키 입니다. 임의로 생성된 50자 문자열을 넣습니다.)"
export RABBITMQ_URL = "RabbitMQ 서버 주소입니다. (예시 : amqp://localhost)"
export GOO_GL_ALI_KEY = "Google URL 단축 서비스 API 키"
export DEBUG = "디버깅 모드 사용 여부 (True / False)"
export DB_USER = 데이터베이스_사용자_이름
export DB_PASSWORD = 데이터베이스_사용자_암호
export DB_NAME = 데이터베이스_이름
export DB_HOST = 데이터베이스_주소(예시:localhost)
export DB_PORT = 데이터베이스_포트
export APP_HOST = "서버를 작동하는 머신이 할당받은 도메인 네임."
export BASEURL = "서버 주소(https://example.com)"
```

다음을 실행하여 서버의 메인 프로세스를 시작합니다.

```
bash start_main.sh
```

다른 명령핼 셸 세션을 열고, 조금 전과 같은 임시로 쓸 환경 변수 설정 후, 다음을 실행하여 Worker 프로세스를 시작합니다.
```
bash start_worker.sh
```

## Docker 를 이용하여 배포

- Docker 를 먼저 설치하세요. (https://docs.docker.com/engine/installation/)
- 배포에 사용할 것들을 Docker Image 로 빌드합니다.
 - Docker Registry 에 업로드 할 예정인 경우, 해당 Registry 의 도메인을 이미지 이름에 포함해야 합니다.
 - 예 : registry.gitlab.com 의 example 계정의 hello 에 업로드 할 경우. -> registry.gitlab.com/example/hello
 - caddy 이미지는 빌드하기 앞서 `Caddyfile` 을 환경에 맞도록 수정해야 합니다.

```
cd caddy
sudo docker build -t example.com/example/caddy:latest . # 이름을 caddy 로, 태그를 latest 로 하여 빌드
cd ../skhufeeds
sudo docker build -t example.com/example/skhufeeds:latest . # 이름을 skhufeeds 로, 태그를 latest 로 하여 빌드
```

- 필요에 따라 Registry 에 빌드 완료한 Docker Image 를 업로드 합니다.
 - 경우에 따라 Registry 에 먼저 로그인 해야 할 수도 있습니다.
```
sudo docker login example.com # 도메인이 example.com 인 Docker Registry 에 로그인
sudo docker push example.com/example/caddy:latest
sudo docker push example.com/example/skhufeeds:latest
```

- 서버에서 Registry 에 로그인 합니다.
```
sudo docker login example.com # 도메인이 example.com 인 Docker Registry 에 로그인
```

- Swarm 모드를 켭니다.
```
sudo docker swarm init
```

- 배포 설정 파일을 `deploy/deploy.yml` 을 참조하여 작성합니다. 작성한 파일을 `*.yml` 확장자로 저장합니다.
- Docker Stack 으로 배포합니다. 추후 새 이미지 적용이 필요한 경우, 동일 명령어를 다시 한번 실행합니다.
```
sudo docker stack deploy --with-registry-auth -c deploy.yml skhufeeds-network
```
