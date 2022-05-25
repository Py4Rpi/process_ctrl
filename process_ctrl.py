"""
Problem 1

1) - Implement a program that will launch a specified process...
2) - ...and periodically (with a provided time interval) collect the following data about it:

    2.1) •	CPU usage (percent);
    2.2) •	Memory consumption: Working Set and Private Bytes (for Windows systems) or Resident Set Size and Virtual Memory Size (for Linux systems);
    2.3) •	Number of open handles (for Windows systems) or file descriptors (for Linux systems).

3) - Data collection should be performed all the time the process is running.
4) - Path to the executable file for the process and time interval between data collection iterations should be provided by user.
5) - Collected data should be stored on the disk.
6) - Format of stored data should support automated parsing to potentially allow, for example, drawing of charts.

"""

import subprocess, csv, psutil


def proc_runner():  # 1) program that will launch a specified process
    file = input('set executable target to run: ')  # 4) Path to the executable file for the process and
    while True:
        try:
            sec = float(input(
                'set interval in seconds: '))  # 4) time interval between data collection iterations provided by user.
            if sec < 0:
                print("Don't use negative input, please")
                continue
            else:
                break
        except ValueError as ex:
            print(ex)
            print('Input only numbers, please')


    proc = subprocess.Popen([file])
    ps = psutil.Process(proc.pid)
    pid = str(proc.pid)

    f = open(f'{ps.name()} pid_{pid} log.csv', 'w', newline='')  # 5) Collected data stored on the disk.
    write = csv.writer(f)  # 6) Format supports automated parsing and drawing of charts.
    write.writerow(['Working Set Memory (kb)', 'Private Memory (kb)', 'Handlers (Qty)', 'CPU Load (%)'])

    while pid:  # 3) Data collection performed all the time the process is running.

        try:  # 2)   Periodically collect the following data:
            proc_cpu = str(ps.cpu_percent(interval=sec) / psutil.cpu_count())  # 2.1) CPU usage (percent)
            mem_ws = str(ps.memory_info().wset / 1024)  # 2.2) Memory consumption - Working Set
            mem_pvt = str(ps.memory_info().private / 1024)  # 2.2) Memory consumption - Private Bytes
            hndl = str(ps.num_handles())  # 2.3) Number of open handles (for Windows systems)

            print('Process name: ' + ps.name() +
                  '  |  Process ID: ' + pid +
                  '  |  Memory Working Set: ' + mem_ws + ' kb' +
                  '  |  Private Memory: ' + mem_pvt + ' kb' +
                  '  |  Handlers: ' + hndl +
                  '  |  CPU Load: ' + '% ' + proc_cpu)

            write.writerow([mem_ws, mem_pvt, hndl, proc_cpu])

        except:
            print('Process stopped')
            f.close()
            break


while True:
    try:
        proc_runner()
    except WindowsError as err:
        print(err)
        print('Try again, please')
