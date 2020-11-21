from django.http import HttpResponse
import datetime
def current_datetime.datetime(request):
    now= datetime.datetime.now()
    html = "<html> <body> Son las: </html> </body>"% now
    return HttpResponse(html)