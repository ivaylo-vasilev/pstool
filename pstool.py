#!/usr/bin/python3

import psutil
from psutil import NoSuchProcess
import argparse
import os
import sys

PLATFORM = sys.platform
STATUS = ["running", "stopped", "sleeping", "zombie", "dead", "idle"]

if PLATFORM == "linux":
    process_attrs = ["name", "pid", "cmdline", "status", "connections"]
    net_connections = 'connections'
elif PLATFORM == "win32":
    process_attrs = ["name", "pid", "cmdline", "status", "net_connections"]
    net_connections = 'net_connections'
else:
    print("pstool: unsupported platform")
    sys.exit(1)

parser = argparse.ArgumentParser(prog="pstool", description="%(prog)s", epilog="(c)2025 Ivaylo Vasilev")
group = parser.add_mutually_exclusive_group()
group.add_argument("--name", help="process name")
group.add_argument("--status", choices=STATUS, help="process status")
group.add_argument("--pid", type=int, help="process PID")
group.add_argument("--kill", nargs="+", type=int, metavar="PID", help="terminate process(es)")
group.add_argument("--killall", metavar="NAME", nargs="+", help="terminate process(es) by name")
parser.add_argument("-v", action="store_true", help="show verbose results")
parser.add_argument("--version", action="version", version=f"%(prog)s 2025.2.1-{PLATFORM}", help="show program version")
args = parser.parse_args()

procs = psutil.pids()

if args.kill:
    for process in args.kill:
        try:
            p = psutil.Process(process)
            if p == os.getpid():
                print(f"PID {os.getpid()}: could not self terminate")
            else:
                p.kill()
                print(f"PID {process} terminated")
        except NoSuchProcess:
            print(f"PID {process} does not exist")
        
    sys.exit(0)
elif args.killall:
    for i in args.killall:
        pids = []
        for proc in psutil.process_iter(["name", "pid"]):
            if i.lower() in proc.info['name'].lower():
                pids.append(int(proc.info['pid']))
        
        for pid in pids:
            try:
                p = psutil.Process(pid)
                if p == os.getpid():
                    print(f"PID {os.getpid()}: could not self terminate")
                else:
                    p.kill()
                    print(f"PID {pid} terminated")
            except NoSuchProcess:
                print(f"PID {pid} does not exist")
    
    sys.exit(0)

counter = 0
totalmemory = 0

if args.name:
    for proc in psutil.process_iter(process_attrs):
        if args.name.lower() in proc.info['name'].lower():
            prcss = psutil.Process(int(proc.info['pid']))
            memusg = (int(prcss.memory_info()[0]) / 1024 / 1024)
            totalmemory += int(prcss.memory_info()[0])
            print(f"PID: {proc.info['pid']} | name: {proc.info['name']} | memory: {memusg:.3f} MB | status: {proc.info['status']}")
            if args.v:
                print(f"cmdline: {proc.info['cmdline']}")
                print(f"net connections: {proc.info[net_connections]}")
                print("==========")
            counter += 1
    if counter == 0:
        print(f"pstool: nothing found for: '{args.name}'")
    else:
        totalmemory = (totalmemory / 1024 / 1024)
        print(f"processes: {counter} | used memory: {totalmemory:.3f} MB")
elif args.status:
    for proc in psutil.process_iter(process_attrs):
        if args.status.lower() in proc.info['status'].lower():
            prcss = psutil.Process(int(proc.info['pid']))
            memusg = (int(prcss.memory_info()[0]) / 1024 / 1024)
            totalmemory += int(prcss.memory_info()[0])
            print(f"PID: {proc.info['pid']} | name: {proc.info['name']} | memory: {memusg:.3f} MB | status: {proc.info['status']}")
            if args.v:
                print(f"cmdline: {proc.info['cmdline']}")
                print(f"net connections: {proc.info[net_connections]}")
                print("==========")
            counter += 1
    if counter == 0:
        print(f"pstool: no processes with status: '{args.status}'")
    else:
        totalmemory = (totalmemory / 1024 / 1024)
        print(f"processes: {counter} | used memory: {totalmemory:.3f} MB")
elif args.pid:
    if psutil.pid_exists(args.pid):
        prcss = psutil.Process(args.pid)
        p = prcss.as_dict()
        memusg = (int(prcss.memory_info()[0]) / 1024 / 1024)
        totalmemory += int(prcss.memory_info()[0])
        print(f"PID: {p['pid']} | name: {p['name']} | memory: {memusg:.3f} MB | status: {p['status']}")
        if args.v:
            print(f"cmdline: {p['cmdline']}")
            print(f"net connections: {p[net_connections]}")
    else:
        print(f"pstool: no process with PID: '{args.pid}'")
else:
    for proc in psutil.process_iter(process_attrs):
        prcss = psutil.Process(int(proc.info['pid']))
        totalmemory += int(prcss.memory_info()[0])
        memusg = (int(prcss.memory_info()[0]) / 1024 / 1024)
        print(f"PID: {proc.info['pid']} | name: {proc.info['name']} | memory: {memusg:.3f} MB | status: {proc.info['status']}")
        if args.v:
            print(f"cmdline: {proc.info['cmdline']}")
            print(f"net connections: {proc.info[net_connections]}")
            print("==========")
        counter += 1
    totalmemory = (totalmemory / 1024 / 1024)
    print(f"processes: {counter} | used memory: {totalmemory:.3f} MB")
