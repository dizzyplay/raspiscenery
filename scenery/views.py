from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.


def main_view(request):
    # get 으로 사진 텀, 날짜를 구해옴
    # 없다면 기본텀은 10
    period = int(request.GET.get('period', '10'))
    request_time = request.GET.get('time', None)

    # 요청 날짜가 없으면 오늘이 기본
    if request_time is not None:
        request_time = str(request_time)
        year = int(request_time[:4])
        month = int(request_time[4:6])
        days = int(request_time[6:8])
        hour = int(request_time[8:10])
        minute = int(request_time[10:12])
        print("{}년 {}월 {}일 {}시 {}분".format(year, month, days, hour, minute))
        now = datetime(year, month, days, hour, minute)
    else:
        now = datetime.now()

    # 사진이 5분단위로 존재 함으로 5분이 아닌 요청의 경우 5분단위로 설정
    m_int = period
    m_delta = timedelta(minutes=period)
    image_list = []
    if now.minute % m_int == 0:
        for i in range(10):
            image_list.append(now.strftime("%Y-%m-%d_%H%M"))
            now -= m_delta
    else:
        get_lid_value = now.minute % m_int
        get_lid_value_delta = timedelta(minutes=get_lid_value)
        now -= get_lid_value_delta
        for i in range(10):
            image_list.append(now.strftime("%Y-%m-%d_%H%M"))
            now -= m_delta

    return render(request, './scenery/main.html', {
        'image_list': image_list,
    })
