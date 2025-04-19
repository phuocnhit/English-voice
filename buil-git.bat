@echo off
setlocal

:: Check if a version parameter is provided
if "%~1"=="" (
    echo Please provide a version number as a parameter.
    echo Example: update_version.bat 1.0.1
    exit /b 1
)

:: Set variables
set "version=%~1"
set "file=version.json"

:: Get current UTC date in ISO 8601 format
for /f %%a in ('powershell -Command "Get-Date -Format s"') do set "date=%%aZ"

:: Write JSON content to version.json
> "%file%" (
    echo {
    echo   "version": "%version%",
    echo   "buildDate": "%date%"
    echo }
)

echo version.json has been updated.

:: Git operations
git add .
git commit -m "Update version to %version%"
git push

echo Git changes pushed.
endlocal
pause
