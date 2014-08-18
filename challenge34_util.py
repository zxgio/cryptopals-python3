from Crypto.Cipher import AES
import base64
import challenge9
import challenge15
import hashlib

class Util:
    def __init__(self, sock):
        f = sock.makefile(mode='rwb', buffering=0)
        self._rfile = f
        self._wfile = f

    def readline(self):
        return self._rfile.readline().strip()

    def readnum(self):
        return int(self.readline())

    def readbytes(self):
        return base64.b64decode(self.readline())

    def writeline(self, line):
        self._wfile.write(line + b'\n')

    def writenum(self, num):
        self.writeline(str(num).encode('ascii'))

    def writebytes(self, bytes):
        self.writeline(base64.b64encode(bytes))

    def derivekey(self, s):
        sha1 = hashlib.sha1()
        sha1.update(str(s).encode('ascii'))
        return sha1.digest()[:16]

    def encrypt(self, key, iv, message):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.encrypt(challenge9.padPKCS7(message.encode('ascii'), 16))

    def decrypt(self, key, iv, encryptedMessage):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return challenge15.unpadPKCS7(cipher.decrypt(encryptedMessage)).decode('ascii')
