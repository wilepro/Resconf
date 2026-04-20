import requests
from rich import print

requests.packages.urllib3.disable_warnings()
headers = {"Accept": "application/yang-data+json"}
url = "https://192.168.1.111/restconf/data/Cisco-IOS-XE-native:native/ntp"

result = requests.get(url=url, headers=headers, auth=("john", "Cisco123"), verify=False)
print(result.text)


********************2 ieme script ********************
import requests
import yaml
from rich import print

requests.packages.urllib3.disable_warnings()
headers = {"Content-Type": "application/yang-data+json"}


def load_configs():
    myconfig = yaml.safe_load(open("R1.yml"))
    return myconfig

def push_config(myconfig):
    url = "https://192.168.1.111/restconf/data/Cisco-IOS-XE-native:native/ntp"
    result = requests.put(url=url, headers=headers, auth=("john", "Cisco123"), json=myconfig, verify=False)
    return result


myconfig = load_configs()
result = push_config(myconfig)
print(result)
