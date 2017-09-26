#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import uuid
import random
import logging
import time
import string

def get_time():
    """ Get current time: YYYY-mm-dd HH:mm:ss:S """
    now = datetime.now()
    return now.isoformat()

def gen_rand_str(length, chars=None):
    return ''.join([random.choice(string.ascii_uppercase) for i in range(length)])


# Loading a template file
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
msg_tpl = env.get_template('template.json')

# List
event_code_list = ['buy', 'drop', 'sell']
platform_list = ["web", "ios", "android"]

# Log file Path
logging.basicConfig(filename="/tmp/app.log", format="%(message)s", level=logging.INFO)

# Generate log with json format
while(True):
    # Generate IDs
    event_code = random.choice(event_code_list)
    id = random.randint(1,999)
    user_id = str(id)
    platform = platform_list[id % 3]
    event_id = gen_rand_str(4) + "%06d" % (random.randint(0,1000000))
    item_id = str(random.randint(1,10))

    msg = msg_tpl.render({
    'eventID': event_id,
    'eventTimestamp': get_time(),
    'eventCode': event_code,
    'userID': user_id,
    'itemID': item_id,
    'platform': platform,
    })
    print (msg)
    logging.info(msg)
    time.sleep(1)
