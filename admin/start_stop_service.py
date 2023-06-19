
import os
import sys
import subprocess

def start_service(service_name):
    try:
        subprocess.run(['systemctl', 'start', service_name], check=True)
        print(f'Service {service_name} started successfully.')
    except subprocess.CalledProcessError:
        print(f'Failed to start service {service_name}.')
        sys.exit(1)

def stop_service(service_name):
    try:
        subprocess.run(['systemctl', 'stop', service_name], check=True)
        print(f'Service {service_name} stopped successfully.')
    except subprocess.CalledProcessError:
        print(f'Failed to stop service {service_name}.')
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python start_stop_service.py <start|stop> <service_name>')
        sys.exit(1)

    action = sys.argv[1]
    service_name = sys.argv[2]

    if action == 'start':
        start_service(service_name)
    elif action == 'stop':
        stop_service(service_name)
    else:
        print('Invalid action. Use start or stop.')
        sys.exit(1)
