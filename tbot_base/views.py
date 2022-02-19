from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .bot import tbot

for module in settings.BOT_HANDLERS:
    __import__(module)


@csrf_exempt
def get_tel_hook(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = request.body.decode('utf-8')
        update = tbot.update(json_data)
        tbot.process_new_updates([update])

        return HttpResponse(status=200)
    raise PermissionDenied
