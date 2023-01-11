@echo off

:: Create virtual environment
if not exist .venv\ (
	python -m venv .venv
)

:: Activate virtual environment
if not defined VIRTUAL_ENV (
	call .venv\Scripts\activate
)

:: Update virtual environment
python -m pip install -U pip setuptools wheel

:: Install dependencies
pip install -r requirements-dev.txt

:: Install pre-commit
pre-commit install
