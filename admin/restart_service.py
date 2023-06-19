
import subprocess
import sys

def restart_service(service_name):
    try:
        subprocess.check_call(['sudo', 'systemctl', 'restart', service_name])
        print(f'Service {service_name} restarted successfully.')
    except subprocess.CalledProcessError:
        print(f'Failed to restart service {service_name}.', file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python restart_service.py <service_name>')
        sys.exit(1)

    service_name = sys.argv[1]
    restart_service(service_name)
