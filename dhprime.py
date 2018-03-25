import os
from base64 import b64decode as b64

HEADER = '-----BEGIN DH PARAMETERS-----\n'
FOOTER = '\n-----END DH PARAMETERS-----'

BITS = 2048
PEM_FILE = "dh.pem"
PRIME_FILE = "safePrime"

os.system("openssl dhparam -out %s -2 %d" % (PEM_FILE, BITS))

s = ""
with open(PEM_FILE, 'r') as f:
    s = f.read()

cert = s[s.find(HEADER) + len(HEADER):s.find(FOOTER)]
prime = b64(cert)[7:-3]

with open(PRIME_FILE, 'w') as f:
    f.write(str(int(prime.encode('hex'), 16)))
