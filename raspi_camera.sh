#! /bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

#5상하반전 후 해당 날짜로 저장
raspistill -vf -hf -o /home/pi/djangotest/djangotest/static/camera/$DATE.jpg

# 장고서버로 보냄
scp /hostserver/$DATE.jpg remote_server:/home/raspiscenery/static/camera/

# 파일삭제
rm /hostserver/$DATE.jpg

