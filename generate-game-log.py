#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import uuid
import random

def get_time():
    """ Get current time: YYYY-mm-dd HH:mm:ss:S """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S.%s") + "%04d" % (now.microsecond // 1000)

# Loading a template file
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
msg_tpl = env.get_template('template.json')

msg_body = {}
platform_list = ["web", "ios", "android"]

for i in range(1, 10):
    platform = random.choice(platform_list)
    event_code = 'event' + "%02d" % (random.randint(1,99))
    user_id = 'user' + "%04d" % (random.randint(1,999))
    session_id = uuid.uuid5(uuid.NAMESPACE_OID, user_id)
    msg = msg_tpl.render({
    'eventCode': event_code,
    'userID': user_id,
    'eventTimestamp': get_time(),
    'sessionID': session_id,
    'platform': platform
    })
    print (msg)
