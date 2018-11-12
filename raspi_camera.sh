#! /bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

#5상하반전 후 해당 날짜로 저장
raspistill -vf -hf -o /라즈베리파이/static/camera/$DATE.jpg

# 장고서버로 보냄 - 호스트 서버와 리모트 서버 주소를 자신에 맞게 바꿔주세요
scp /라즈베리파이/$DATE.jpg 장고프로젝트서버:/장고프로젝트/raspiscenery/static/camera/

# 파일삭제
rm /라즈베리파이/$DATE.jpg

