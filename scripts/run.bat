@echo off

:: Activate virtual environment
if not defined VIRTUAL_ENV (
	call .venv\Scripts\activate
)

echo No Application Found
