# Makefile
SHELL = /bin/bash

run:
	uvicorn app.main:app --reload 