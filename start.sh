#!/usr/bin/bash

source venv/bin/activate

nohup python3 flask/home.py 2&1> nohup.out &
