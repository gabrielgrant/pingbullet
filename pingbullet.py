#!/usr/bin/env python

"""
Pingbullet

Regularly pings you via Pushbullet
"""

import datetime
import json
import os
from urlparse import urlparse, urlunparse

import requests

# load the configuration env vars defined in app.json
env_vars = json.load(open('app.json'))['env'].keys()
for e in env_vars:
    globals()[e] = os.environ.get(e)
if not PUSHBULLET_ACCESS_TOKEN:
    raise RuntimeError('PUSHBULLET_ACCESS_TOKEN is a required parameter')

PUSHBULLET_API_URL = 'https://api.pushbullet.com/v2/pushes'

def send_push(title, body, url=None):
    headers = {'Access-Token': PUSHBULLET_ACCESS_TOKEN}
    data = {
        'title': title,
        'body': body,
    }
    if url:
        data['type'] = 'link'
        data['url'] = url
    else:
        data['type'] =  'note'
    r = requests.post(PUSHBULLET_API_URL, headers=headers, data=data)

def main():
    if ACTIVE == 'true':
        send_push(PUSH_TITLE, PUSH_BODY, PUSH_URL)
    

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
