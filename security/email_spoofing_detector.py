
import re
import dns.resolver
import socket
import requests

def check_mx_record(domain):
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        return mxRecord
    except:
        return None

def check_spf_record(domain):
    try:
        records = dns.resolver.resolve(domain, 'TXT')
        for rdata in records:
            if "v=spf" in str(rdata):
                return True
        return False
    except:
        return False

def check_dmarc_record(domain):
    try:
        records = dns.resolver.resolve('_dmarc.'+domain, 'TXT')
        for rdata in records:
            if "v=DMARC" in str(rdata):
                return True
        return False
    except:
        return False

def check_email_spoofing(email):
    domain = email.split('@')[-1]
    mx_record = check_mx_record(domain)
    spf_record = check_spf_record(domain)
    dmarc_record = check_dmarc_record(domain)

    if mx_record and spf_record and dmarc_record:
        return "Email is not spoofed"
    else:
        return "Email may be spoofed"

def main():
    email = input("Enter the email to check: ")
    result = check_email_spoofing(email)
    print(result)

if __name__ == "__main__":
    main()
