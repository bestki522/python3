def get_ssl_info(hostname, port=443):
    """function to grab ssl information from remote host, return dict type object"""

    import socket
    import ssl
    context = ssl.create_default_context()
    # Create SSL socket with IPv4 and ssl port
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)

    # 3 second timeout because Lambda has runtime limitations
    try:
        conn.settimeout(3.0)
        conn.connect((hostname, port))
        ssl_info = conn.getpeercert()
        return ssl_info
    except ConnectionRefusedError as e:
        return e

def get_crt(hostname1):
    """function to grab ssl crt from remote host"""

    import ssl
    ssl_crt = ssl.get_server_certificate((hostname1, 443))
    return ssl_crt


if __name__ == '__main__':
    import json
    domain_name = 'google.com.vn'
    info = get_ssl_info(domain_name)
    print(info)  # print all dictionary key-value pairs
    print(info['notAfter'])  # print the value of notAfter key
    print(info['notBefore'])  # print the value of notBefore key
    #print(info['commonName'])   # print the value of commonName key

    result = json.loads(info, indent=5)
    #cert = ssl.get_server_certificate((domain_name, 443))
    #print(cert)
