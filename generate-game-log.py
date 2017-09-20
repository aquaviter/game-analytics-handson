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

# List
eventcode_list = ['buy']
platform_list = ["web", "ios", "android"]

# Log file Path
logging.basicConfig(filename="/tmp/app.log", format="%(message)s", level=logging.INFO)

# Generate log with json format
while(True):
    # Generate IDs
    event_code = random.choice(eventcode_list)
    platform = random.choice(platform_list)
    user_id = 'user' + "%03d" % (random.randint(1,99))
    item_id = 'item' + "%03d" % (random.randint(1,99))
    transaction_id = uuid.uuid1()

    msg = msg_tpl.render({
    'eventCode': event_code,
    'userID': user_id,
    'eventTimestamp': get_time(),
    'transactionID': transaction_id,
    'platform': platform,
    'itemID': item_id
    })
    print (msg)
    logging.info(msg)
    time.sleep(5)
