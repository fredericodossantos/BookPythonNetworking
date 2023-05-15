import sys
import ssl
import socket

try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)

host = 'www.rfc-editor.org'
port = 443
context = ssl.create_default_context()
sock = socket.create_connection((host, port))
sock = context.wrap_socket(sock, server_hostname=host)

req = ('GET https://{host}/rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
       'Host: {host}\r\n'
       'User-Agent: Python {version}\r\n'
       'Connection: close\r\n'
       '\r\n')

req = req.format(rfcnum=rfc_number, host=host, version=sys.version_info[0])
sock.sendall(req.encode('ascii'))

rfc_bytes = bytearray()

while True:
    buf = sock.recv(4096)
    if not len(buf):
        break
    rfc_bytes += buf

rfc = rfc_bytes.decode('utf-8')
print(rfc)
