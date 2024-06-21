import platform
import psutil
import shutil
import socket
import netifaces
import requests
import pyudev
import shutil
import os

def sysinfo():
    print("System Information:")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"CPU: {platform.processor()}")
    print(f"Python Version: {platform.python_version()}")

    print("\nCPU Information:")
    print(f"CPU Count: {psutil.cpu_count()}")
    print(f"CPU Utilization: {psutil.cpu_percent(interval=1)}%")
    print(f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz")

    print("\nMemory Information:")
    mem = psutil.virtual_memory()
    print(f"Total Memory: {round(mem.total / (1024.0 ** 3), 2)} GB")
    print(f"Available Memory: {round(mem.available / (1024.0 ** 3), 2)} GB")
    print(f"Used Memory: {round(mem.used / (1024.0 ** 3), 2)} GB")
    print(f"Memory Usage: {mem.percent}%")

    print("\nDisk Information:")
    disk = shutil.disk_usage("/")
    print(f"Total Disk Space: {round(disk.total / (1024.0 ** 3), 2)} GB")
    print(f"Used Disk Space: {round(disk.used / (1024.0 ** 3), 2)} GB")
    print(f"Free Disk Space: {round(disk.free / (1024.0 ** 3), 2)} GB")
    print(f"Disk Usage: {round(disk.used / disk.total * 100, 2)}%")

    print("\nNetwork Information:")
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {round(net_io.bytes_sent / (1024.0 ** 2), 2)} MB")
    print(f"Bytes Received: {round(net_io.bytes_recv / (1024.0 ** 2), 2)} MB")

    print("\nNetwork Interfaces:")
    for interface in netifaces.interfaces():
        print(f"Interface: {interface}")
        try:
            addr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
            print(f"IP Address: {addr}")
        except (ValueError, IndexError):
            print("IP Address: N/A")
        try:
            netmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
            print(f"Netmask: {netmask}")
        except (ValueError, IndexError):
            print("Netmask: N/A")
        try:
            broadcast = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['broadcast']
            print(f"Broadcast: {broadcast}")
        except (ValueError, IndexError):
            print("Broadcast: N/A")
        print()

    print("\nConnected Devices:")
    context = pyudev.Context()
    for device in context.list_devices(subsystem='input'):
        if 'ID_INPUT_KEYBOARD' in device.properties:
            print(f"Keyboard: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_MOUSE' in device.properties:
            print(f"Mouse: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_TOUCHPAD' in device.properties:
            print(f"Touchpad: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_TOUCHSCREEN' in device.properties:
            print(f"Touchscreen: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_TABLET' in device.properties:
            print(f"Tablet: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_JOYSTICK' in device.properties:
            print(f"Joystick: {device.get('ID_MODEL')}")
        elif 'ID_INPUT_VIDEO_DISPLAY' in device.properties:
            print(f"Monitor: {device.get('ID_MODEL')}")

    print("\nDisplay Information:")
    try:
        edid = os.popen('get-edid').read()
        edid_lines = edid.split('\n')
        for line in edid_lines:
            if line.startswith('Manufacturer:'):
                print(f"Manufacturer: {line.split(':')[1].strip()}")
            elif line.startswith('Monitor Name:'):
                print(f"Model: {line.split(':')[1].strip()}")
            elif line.startswith('Detailed Timing Description:'):
                width, height = line.split(',')[0].split()[1].split('x')
                refresh_rate = line.split(',')[1].strip().split()[0]
                print(f"Resolution: {width}x{height}")
                print(f"Refresh Rate: {refresh_rate} Hz")
    except:
        print("Unable to retrieve display information.")

    print("\nOther Information:")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Public IP Address: {requests.get('https://api.ipify.org').text}")