# pstool
Process information tool for Linux and Windows.
---

**pstool** is a CLI program whose purpose is to list the loaded processes in a Linux or Windows based system and to give detailed information about each one of them, such as the **process ID**, **executable name**, **command line parameters** with which the process was started, and the **network or Internet connections** of the process if any. The program can show the information for a specific process or group of processes of a program, giving you the ability to search by *name*, *PID (process ID)*, or *process status*. **pstool** has an option for a verbose results.

**[UPDATE]** 2025-05-02: (v.2025.3) Cleaning some differences between Linux and Windows versions, like the keyword for "net_connections", which was "connections" with previous versions of **psutil** library. Changed the way of how the total number of loaded processes is displayed if **pstool** is used without additional command line arguments. In Linux version the total amount of used memory is currently *not* displayed along with the number of loaded processes.

**Usage:**
`$pstool    -> list all the loaded processes`

Optional arguments:
```
  --name NAME                                            process name
  --status {running,stopped,sleeping,zombie,dead,idle}   process status
  --pid PID                                              process PID
  -v                                                     show verbose results
```
The current version of **pstool** can also terminate a single process or all loaded processes of a given program. The following optional arguments are related to process(es) termination:
```
  --kill PID [PID ...]        terminate process(es)
  --killall NAME [NAME ...]   terminate process(es) by name
```
