import OpenSSL
import ssl, socket
import argparse

def get_certificate(hostname, port):
    context = ssl.create_default_context()
    conn = socket.create_connection((hostname, port))
    sock = context.wrap_socket(conn, server_hostname=hostname)
    certificate = ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))
    return OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)

def print_certificate_info(certificate):
    subject = certificate.get_subject()
    issuer = certificate.get_issuer()

    print("Subject: ", subject.CN)
    print("Issuer: ", issuer.CN)
    print("Version: ", certificate.get_version())
    print("Serial Number: ", certificate.get_serial_number())
    print("Not Before: ", certificate.get_notBefore())
    print("Not After: ", certificate.get_notAfter())

def main():
    parser = argparse.ArgumentParser(description='SSL Certificate Checker')
    parser.add_argument('hostname', type=str, help='Hostname to check')
    parser.add_argument('port', type=int, help='Port to check')
    args = parser.parse_args()

    certificate = get_certificate(args.hostname, args.port)
    print_certificate_info(certificate)

if __name__ == "__main__":
    main()
