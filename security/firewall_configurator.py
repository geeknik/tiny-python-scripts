
import os

def configure_firewall():
    print("Configuring Firewall...")
    os.system('iptables -A INPUT -i lo -j ACCEPT')
    os.system('iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT')
    os.system('iptables -A INPUT -p tcp --dport 22 -j ACCEPT')
    os.system('iptables -A INPUT -p tcp --dport 80 -j ACCEPT')
    os.system('iptables -A INPUT -p tcp --dport 443 -j ACCEPT')
    os.system('iptables -P INPUT DROP')
    os.system('iptables -P FORWARD DROP')
    os.system('iptables -P OUTPUT ACCEPT')
    print("Firewall Configuration Completed.")

def save_firewall_rules():
    print("Saving Firewall Rules...")
    os.system('iptables-save > /etc/iptables/rules.v4')
    print("Firewall Rules Saved.")

def main():
    configure_firewall()
    save_firewall_rules()

if __name__ == "__main__":
    main()
```
This script configures a basic firewall using iptables, allowing only loopback, established connections, and traffic on ports 22 (SSH), 80 (HTTP), and 443 (HTTPS). It then saves these rules so they persist after a reboot. Please note that this script needs to be run as root.