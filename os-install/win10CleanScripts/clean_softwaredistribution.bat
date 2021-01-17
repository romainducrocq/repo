net stop wuauserv
del /q /s C:\Windows\SoftwareDistribution\*
net start wuauserv
pause

net stop wuauserv
net stop cryptSvc
net stop bits
net stop msiserver
rmdir /q /s C:\Windows\SoftwareDistribution.old
ren C:\Windows\SoftwareDistribution SoftwareDistribution.old
rmdir /q /s C:\Windows\System32\catroot2.old
ren C:\Windows\System32\catroot2 catroot2.old
net start wuauserv
net start cryptSvc
net start bits
net start msiserver
pause