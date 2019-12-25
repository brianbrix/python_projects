import base64
s=open('outt.txt', 'rb').read().decode()
img =open('outt.png', 'wb+')
img.write(s.codecs.decode('base64'))
img.close()
