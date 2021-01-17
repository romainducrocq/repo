Dism.exe /online /Cleanup-Image /AnalyzeComponentStore
echo.&echo.&choice /n /c YN /m "Clean WinSxS [Y,N]?" & if errorlevel 2 exit
Dism.exe /online /Cleanup-Image /StartComponentCleanup
Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase
Dism.exe /online /Cleanup-Image /SPSuperseded
pause


