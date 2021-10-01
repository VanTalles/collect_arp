#!/usr/bin/python3

from netmiko import ConnectHandler
import config
import textfsm

hosts = []
hosts2 = []
hosts3 = []

def parse_result(result1):
    with open('alliedtelesis_show_arp.textfsm') as template:
        fsm = textfsm.TextFSM(template)
        result = fsm.ParseText(result1)
    return result

def get_arp_data(host):
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': config.username,
        'password': config.password,
    }
    net_connect = ConnectHandler(**device)
    res = net_connect.send_command("show arp", use_textfsm = True)
    return host,parse_result(res)


def get_arp_data2(host):
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': config.username,
        'password': config.password,
    }
    net_connect = ConnectHandler(**device)
    res = net_connect.send_command("show ip arp", use_textfsm = True)
    return host,res

def get_arp_data3(host):
    device = {
        'device_type': 'cisco_ios_telnet',
        'host': host,
        'username': config.username,
        'password': config.password,
    }
    net_connect = ConnectHandler(**device)
    res = net_connect.send_command("show ip arp", use_textfsm = True)
    return host,res




result_list = []


for host in hosts:
    h1,res = get_arp_data(host)
    for r1 in res:
        result_list.append({'address':r1[0],'mac':r1[1]})

for host in hosts2:
    h1,res = get_arp_data2(host)
    for r1 in res:
        result_list.append({'address':r1['address'],'mac':r1['mac']})


for host in hosts3:
    h1,res = get_arp_data3(host)
    for r1 in res:
        result_list.append({'address':r1['address'],'mac':r1['mac']})



print (len(result_list))


def1 = 0

for r1 in result_list:
   if '10.50.' in r1['address']:
       def1 += 1

print (def1)
