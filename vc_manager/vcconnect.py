#!/usr/bin/env python3

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s = requests.Session()
s.verify = False


# Function to get the vCenter server session
def get_vc_session(vcip, username, password):
    s.post('https://' + vcip + '/rest/com/vmware/cis/session', auth=(username, password))
    return s


# Function to get all the VMs from vCenter inventory
def get_vms(vcip):
    vms = s.get('https://' + vcip + '/rest/vcenter/vm')
    return vms


# Function to power on particular VM
def poweron_vm(vmmoid, vcip):
    s.post('https://' + vcip + '/rest/vcenter/vm/' + vmmoid + '/power/start')


# Function to power off particular VM
def poweroff_vm(vmmoid, vcip):
    s.post('https://' + vcip + '/rest/vcenter/vm/' + vmmoid + '/power/stop')


# Function to delete vm
def delete_vm(vmoid, vcip):
    s.delete('https://' + vcip + '/rest/vcenter/vm/' + vmoid)
