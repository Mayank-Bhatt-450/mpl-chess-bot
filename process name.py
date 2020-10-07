'''
import wmi
c = wmi.WMI ()

for process in c.Win32_Process ():
  print (process.ProcessId, process.Name)
'''
'''
import win32com.client
wmi=win32com.client.GetObject('winmgmts:')
for p in wmi.InstancesOf('win32_process'):
    print (p.Name, p.Properties_('ProcessId'), \
        int(p.Properties_('UserModeTime').Value)+int(p.Properties_('KernelModeTime').Value))
    children=wmi.ExecQuery('Select * from win32_process where ParentProcessId=%s' %p.Properties_('ProcessId'))
    for child in children:
        print ('\t',child.Name,child.Properties_('ProcessId'), \
            int(child.Properties_('UserModeTime').Value)+int(child.Properties_('KernelModeTime').Value))
'''
import os
import psutil
import time
def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''
 
    listOfProcessObjects = []
 
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
 
    return listOfProcessObjects;
print(findProcessIdByName('Google Chrome'))
3
4
5
6
7
8
9
10
11
12
# Find PIDs od all the running instances of process that contains 'chrome' in it's name
listOfProcessIds = findProcessIdByName('chrome')
 
if len(listOfProcessIds) > 0:
   print('Process Exists | PID and other details are')
   for elem in listOfProcessIds:
       processID = elem['pid']
       processName = elem['name']
       processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
       print((processID ,processName,processCreationTime ))
else :
   print('No Running Process found with given text')
