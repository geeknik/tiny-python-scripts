
import whois
import sys

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python whois_lookup.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    result = whois_lookup(domain)
    print(result)

if __name__ == "__main__":
    main()
