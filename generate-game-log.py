#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import uuid
import random
import logging
import time

def get_time():
    """ Get current time: YYYY-mm-dd HH:mm:ss:S """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S.") + "%04d" % (now.microsecond // 1000)

# Loading a template file
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
msg_tpl = env.get_template('template.json')

# Platform List
platform_list = ["web", "ios", "android"]

# Log file Path
logging.basicConfig(filename="/tmp/app.log", format="%(message)s", level=logging.INFO)

# Generate log with json format
while(True):
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
    logging.info(msg)
    time.sleep(5)
