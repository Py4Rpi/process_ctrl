# PROCESS CONTROL PROGRAM (WINDOWS)

Test task program

![alt text](https://github.com/Py4Rpi/process_ctrl/blob/master/screen.jpg)

## Description

Hello!

This is my test task from employer. It is a simple program for Windows 10 that launches a specified process and
periodically (with a provided time interval) collects the process CPU usage, memory consumption and number of open handles.
 
## Getting Started

### Dependencies

I used Python 3.8. in this project.

There is only one external librariy to be used - Psutil. Othres are native python modules.

### Installing

To install the programm you can just download it as a ZIP file or use "gh repo clone Py4Rpi/process_ctrl" command. 
Then just copy the process_ctrl.py file to convenient folder. Ensure that Python 3.8 is installed on your Windows.
Then install Psutil library with "pip install psutil" command in your cmd.

### Executing program

* When dependencies and installing steps are completed you can just open terminal, go to dir with process_ctrl.py and run it :

```
python process_ctrl.py
```

If all goes well then program will send your request for input the executable file which you want to start with it.
Keep in mind that program won't run non executable files and docements.

At next step it will request an interval of monitoring iterations in seconds. Only positive nubmers can be used here.
Then the process will run and program will print all data in console. It saves the separate csv log for each session
as well. The log will be saved at the same directory with program. 

Please, do not relay on Windows taskmanager to compare the data as it apears that taskmgr shows incorect values at 
some fields. Use Process Explorer in case you want to double check the accuracy of calculated values by program >
https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer

The program will stopped right after you stop the runned process. As it mentioned before, all collected data will 
be stored at csv log file with name of executed process and it's ID.

## Help

If any troubles you can use Issue Tracker to notify me.

Have a nice coding :)

## Version History

* 0.1
    * Initial Release

## License

There is no any licence. It is a test task project.
