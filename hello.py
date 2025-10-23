#!/usr/bin/python3
import psutil

print('Hello world')

# 获取 CPU 使用率（每秒更新一次）
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

# 获取内存信息
mem = psutil.virtual_memory()
print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
print(f"Used Memory: {mem.used / (1024**3):.2f} GB")
print(f"Memory Usage: {mem.percent}%")

# 获取磁盘使用情况（根目录）
disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024**3):.2f} GB")
print(f"Disk Usage: {disk.percent}%")

