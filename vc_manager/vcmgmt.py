#!/usr/bin/env python3
# Description:Get VMs and their moid using vCenter server REST API.

from . import vcconnect
import json
import argparse


# Get vCenter server session, pass vcenter name & password.
vcip = "YOUR_VCENTER_FQDN:443"
vcuser = "YOUR_VCENTER_USER"
vcpass = "YOUR_VCENTER_PASSWORD"

vcsession = vcconnect.get_vc_session(
    vcip, vcuser, vcpass)


# Get all the VMs.
vms = vcconnect.get_vms(vcip)


# Get all VMs
def get_total_vms():
    vm_response = json.loads(vms.text)
    json_data = vm_response["value"]
    with open('vminventory.txt', 'w') as f:
        for vm in json_data:
            f.write(vm.get("name") + " :: " + vm.get("vm") + "\n")
    print("All VMs updated in file vminventory.txt.")
    f.close()
    return len(open('vminventory.txt').readlines())


# Write user VMs to 'my_vms.txt'
def get_user_vms(keyword):
    vm_response = json.loads(vms.text)
    json_data = vm_response["value"]
    myvms = open('my_vms.txt', 'w')
    for vm in json_data:
        if keyword in vm.get("name"):
            print(vm.get("name"))
            myvms.write(vm.get("name") + " :: " + vm.get("vm") + "\n")
    myvms.close()
    return len(open('my_vms.txt').readlines())


# Reset VMs
def reset_user_vms(keyword):
    print("Doing a hard reset on your VMs.")
    vm_response = json.loads(vms.text)
    json_data = vm_response["value"]
    for vm in json_data:
        if keyword in vm.get("name"):
            print("Rebooting %s" % vm.get("name"))
            if vm.get("power_state") == "POWERED_ON":
                vcconnect.poweroff_vm(vm.get("vm"), vcip)
                vcconnect.poweron_vm(vm.get("vm"), vcip)


def power_off_user_vms(keyword):
    print("Powering off your VMs.")
    vm_response = json.loads(vms.text)
    json_data = vm_response["value"]
    for vm in json_data:
        if keyword in vm.get("name"):
            if vm.get("power_state") == "POWERED_ON":
                vcconnect.poweroff_vm(vm.get("vm"), vcip)


def delete_user_vms(keyword):
    vm_response = json.loads(vms.text)
    json_data = vm_response["value"]
    for vm in json_data:
        if keyword in vm.get("name"):
            if vm.get("power_state") == "POWERED_ON":
                vcconnect.poweroff_vm(vm.get("vm"), vcip)
            else:
                pass
            print("Deleting %s" % vm.get("name"))
            vcconnect.delete_vm(vm.get("vm"), vcip)


def main():
    parser = argparse.ArgumentParser(description='Perform actions on vms')
    subparsers = parser.add_subparsers(dest="command")

    vms_parser = subparsers.add_parser(
        "vms", help="vms sub command.")
    vms_parser.add_argument(
        "--show", action="store_true", help="Show machines.")
    vms_parser.add_argument(
        "--reboot", action="store_true", help="Reboot machines.")
    vms_parser.add_argument(
        "--destroy", action="store_true", help="Destroy Machines.")
    vms_parser.add_argument(
        "--keyword", dest="keyword", help="Search vsphere for virtual machines with names containing a keyword.")

    args = parser.parse_args()

    if args.command == "vms":
        if args.show:
            if args.keyword:
                total_user_vms = get_user_vms(args.keyword)
                print(str("There are %i virtual machines matching keyword \"%s\"." % (
                    total_user_vms, args.keyword)))
            else:
                total_vms = get_total_vms()
                print("%i virtual machines in total." % total_vms)
        elif args.reboot:
            print("\n")
            get_user_vms(args.keyword)
            print("\n")
            ans = input(
                    "Are you sure you want to reboot these VMs?\n>")
            if ans == "yes":
                reset_user_vms(args.keyword)
            else:
                print("Not destroying any VMs. Exiting")
        elif args.destroy:
            print("\n")
            get_user_vms(args.keyword)
            ans = input(
                "Are you sure you want to delete these VMs?\n(Only yes will delete them.)\n>")
            if ans == "yes":
                delete_user_vms(args.keyword)
            else:
                print("Not destroying any VMs. Exiting.")


if __name__ == "__main__":
    main()
