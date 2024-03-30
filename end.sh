#!/usr/bin/bash

pids=$(lsof -t -i :5003)

if [ -n "$pids" ]; then
    # 逐个终止对应端口的进程
    for pid in ${pids}; do
        kill -9 "$pid"
        echo "Process with PID $pid has been terminated."
    done
else
    echo "No process found using port"
fi