from datetime import datetime, timedelta

import pytz
from django.http import HttpResponse
from app01.sms.tasks import send_sms,send_sms2

# Create your views here.
def tasks(request):
    # send_sms.delay("110")
    # send_sms2.delay("119")
    local_tz = pytz.timezone('Asia/Shanghai')
    ctime = datetime.now(local_tz)
    print(ctime)
    time_delay = timedelta(seconds=10)
    task_time = ctime + time_delay
    result = send_sms.apply_async(["911", ], eta=task_time)
    print(result.id)
    return HttpResponse("ok")