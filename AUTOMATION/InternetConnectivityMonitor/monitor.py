import requests
import socket
import platform
import subprocess
import time

# List of websites
websites = ['http://google.com', 'http://facebook.com', 'http://twitter.com']

# Check internet connectivity
def check_internet():
    for website in websites:
        try:
            response = requests.get(website, timeout=10)
            if response.status_code == 200:
                print("\033[92mConnected to {}\033[0m".format(website))
                return True
        except requests.ConnectionError as e:
            print("\033[91mFailed to connect to {}: {}\033[0m".format(website, e))
            break  # Stop further attempts if one website fails
    return False

# Diagnose network issues
def diagnose_issue():
    # Flush DNS cache
    try:
        if platform.system() == 'Windows':
            subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("\033[92mDNS cache flushed.\033[0m")
        elif platform.system() in ['Darwin']:
            subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"], check=True)
            subprocess.run(["sudo", "dscacheutil", "-flushcache"], check=True)
            print("\033[92mDNS cache flushed.\033[0m")
        elif platform.system() in ['Linux']:
            subprocess.run(["sudo", "systemctl", "restart", "networking"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("\033[92mDNS cache flushed.\033[0m")
        else:
            print("\033[91mUnsupported platform for DNS cache flushing.\033[0m")
    except subprocess.CalledProcessError as e:
        print("\033[91mFailed to flush DNS cache: {}\033[0m".format(e))

    # Check DNS resolution
    try:
        socket.gethostbyname('google.com')
        print("\033[92mDNS resolution successful.\033[0m")
    except socket.gaierror:
        print("\033[91mDNS resolution failed. Check DNS settings.\033[0m")

    # Check DNS hijacking
    try:
        dns_response = socket.gethostbyname('example.com')
        if dns_response != '93.184.216.34':
            print("\033[93mDNS hijacking detected.\033[0m")
    except socket.gaierror:
        print("\033[91mDNS resolution failed. Check DNS settings.\033[0m")

    # Check if proxy is blocking connections
    try:
        response = requests.get("http://example.com", timeout=10)
        if response.status_code == 200:
            print("\033[92mProxy is not blocking connections.\033[0m")
    except requests.ConnectionError:
        print("\033[91mConnection Error Occurred, Proxy could be blocking connection. \033[0m")

    # Check general network connectivity
    try:
        socket.create_connection(("google.com", 80), timeout=10)
        print("\033[92mIPv4 network connectivity is fine.\033[0m")
    except OSError:
        print("\033[91mIPv4 network connectivity issue. Check network settings or firewall.\033[0m")

    # Check ipv6 ping
    if platform.system() != 'Windows':  # Windows does not support IPv6 ping easily
        try:
            subprocess.run(["ping", "-c", "1", "-6", "ipv6.google.com"], timeout=10, check=True)
            print("\033[92mIPv6 network connectivity is fine.\033[0m")
        except subprocess.CalledProcessError:
            print("\033[91mIPv6 network connectivity issue. Check network settings or firewall.\033[0m")
        except subprocess.TimeoutExpired:
            print("\033[91mIPv6 ping timeout.\033[0m")

    # Check if ping is working
    try:
        if platform.system() == 'Windows':
            subprocess.run(["ping", "-n", "1", "8.8.8.8"], timeout=10, check=True)
        else:
            subprocess.run(["ping", "-c", "1", "8.8.8.8"], timeout=10, check=True)
        print("\033[92mPing is up.\033[0m")
    except subprocess.CalledProcessError:
        print("\033[91mUnable to ping. Probably Internet is not working, Check firewall settings if any.\033[0m")
    except subprocess.TimeoutExpired:
        print("\033[91mUnable to ping. Internet is not working.\033[0m")

    # Check Captive portals
    try:
        response = requests.get("http://clients3.google.com/generate_204", timeout=10)
        if response.status_code == 204:
            print("\033[92mNo captive portal detected.\033[0m")
        else:
            print("\033[93mCaptive portal detected.\033[0m")
    except requests.ConnectionError:
        print("\033[91mFailed to check for captive portal.\033[0m")

    # Check certificate
    try:
        response = requests.get("https://google.com", timeout=10)
        print("\033[92mSSL certificate check successful.\033[0m")
    except requests.exceptions.SSLError:
        print("\033[91mSSL certificate check failed. Check SSL certificates.\033[0m")
    except requests.ConnectionError:
        print("\033[91mFailed to check SSL certificate.\033[0m")

#Restart Wi-Fi connection
def restart_wifi():
    system = platform.system()
    if system == 'Windows':
        try:
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "disabled"], check=True)
            time.sleep(5)
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "enabled"], check=True)
        except subprocess.CalledProcessError as e:
            print("\033[91mFailed to restart Wi-Fi on Windows: {}\033[0m".format(e))
    elif system == 'Linux':
        try:
            subprocess.run(["sudo", "systemctl", "restart", "network-manager"], check=True)
        except subprocess.CalledProcessError as e:
            print("\033[91mFailed to restart Wi-Fi on Linux: {}\033[0m".format(e))
    elif system == 'Darwin':  # macOS
        try:
            subprocess.run(["networksetup", "-setairportpower", "en0", "off"], check=True)
            time.sleep(5)
            subprocess.run(["networksetup", "-setairportpower", "en0", "on"], check=True)
        except subprocess.CalledProcessError as e:
            print("\033[91mFailed to restart Wi-Fi on macOS: {}\033[0m".format(e))
    else:
        print("\033[91mUnsupported platform.\033[0m")

#Check internet connectivity every 10 seconds
while True:
    if not check_internet():
        print("\033[91mInternet is down. Diagnosing the issue...\033[0m")
        diagnose_issue()
        print("\033[93mAttempting to restart Wi-Fi...\033[0m")
        restart_wifi()
        time.sleep(10)  # Allow time for Wi-Fi to reconnect
        if check_internet():
            print("\033[92mWi-Fi restarted successfully.\033[0m")
        else:
            print("\033[91mFailed to restart Wi-Fi or connect to the internet.\033[0m")
    else:
        print("\033[92mInternet is up and running.\033[0m")

    time.sleep(10)  # Wait for 10 seconds before checking again
