import platform
import psutil

def get_system_info():
    return f"""
System: {platform.system()} {platform.release()}
CPU: {platform.processor()}
RAM: {psutil.virtual_memory().total // (1024**2)} MB
Uptime: {psutil.boot_time()}
"""
