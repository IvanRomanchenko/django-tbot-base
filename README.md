# django-tbot-base  
#### _Django Telegram bot base config_  

## Installation:
```sh
pip install django-tbot-base
```

## Setting up   
`YourProject/settings.py`
```python
# Application definition
INSTALLED_APPS = [
    'tbot_base',
    ...
]

# Add your bot handlers in order of priority
BOT_HANDLERS = [
   'tbot.handlers',
]
```

`YourProject/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tbot_base.urls')),  # include webhook url
]
```

## Usage
### Handlers
`YourProject/tbot/handlers.py`
```python
from telebot import types
from telebot.apihelper import ApiTelegramException

from tbot_base.bot import tbot


@tbot.message_handler(func=lambda message: True)
def text_messages(message: types.Message):
    tbot.send_message(message.from_user.id, 'Hello!')


@tbot.callback_query_handler(func=lambda call: True)
def callback_inline(call: types.CallbackQuery):
    tbot.send_message(call.from_user.id, 'Hello!')

    # remove the "clock" on the inline button
    try:
        tbot.answer_callback_query(callback_query_id=call.id, text='')
    except ApiTelegramException:
        pass
```
