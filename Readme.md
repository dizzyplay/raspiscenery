필요도구
==
- crontab
- django

##라즈베리파이에서
1. 라즈베리파이에 카메라를 연결합니다.
2. 사진을 찍기위해 shell script를 만듭니다
[]raspistill.sh참고]
3. crontab을 이용해 주기적으로 사진을 찍고
scp로 django가 설치된 서버로 보냅니다. 사진은 보낸후 삭제됩니다.

##Django 에서 
1. db를 사용하지 않기 때문에 따로 migrate는 필요 없습니다.
2. 찍힌 사진 파일은 /static/camera에 날짜시간별로 저장됩니다.
3. pip install -r requirements.txt
4. python manage.py runserver


