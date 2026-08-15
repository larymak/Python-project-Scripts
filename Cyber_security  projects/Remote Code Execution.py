import requests
from subprocess import Popen, PIPE


router_host = "http://192.168.1.1"
authorization_header = "YWRtaW46QWRtMW5ATDFtMyM="

lhost = "lo"
lport = 80
payload_port = 81


def get_session():
    """
    Retrieves a session value from the router response.
    """

    url = f"{router_host}/admin/ping.html"

    headers = {
        "Authorization": f"Basic {authorization_header}"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    if "&sessionKey=" not in response.text:
        raise ValueError("Session key not found in response")

    session_key = response.text.split("&sessionKey=")[1].split("'")[0]

    return session_key


def send_request(payload):
    """
    Sends a request with the provided data.
    """

    url = router_host + "/admin/pingHost.cmd"

    headers = {
        "Authorization": f"Basic {authorization_header}"
    }

    params = {
        "action": "add",
        "targetHostAddress": payload,
        "sessionKey": get_session()
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    return response.text


def main():

    try:
        print("Starting program")

        # placeholder for test data
        test_payload = "test"

        result = send_request(test_payload)

        print("Request completed")
        print(result)

    except requests.RequestException as error:
        print(f"Network error: {error}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
