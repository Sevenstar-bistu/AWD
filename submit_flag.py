#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def submit_flag(flag, token):
    url = "http://172.16.200.20:9000/submit_flag/"
    failed = ''
    data = {
        "flag":flag,
        "token":token
    }
    print "[+] Submiting flag : [%s]" % (data)
    response = requests.post(url, data=data)
    content = response.content
    print "[+] Content : %s" % (content)
    if failed in content:
        print "[-] failed!"
        return False
    else:
        print "[+] Success!"
        return True
