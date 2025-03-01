# pstool
Process information tool for Linux and Windows.
---

**pstool** is a CLI program whose purpose is to list the loaded processes in a Linux or Windows based system and to give detailed information about each one of them, such as the **process ID**, **executable name**, **command line parameters** with which the process was started, and the **network or Internet connections** of the process if any. The program can show the information for a specific process or group of processes of a program, giving you the ability to search by *name*, *PID (process ID)*, or *process status*. **pstool** has an option for a verbose results.

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
