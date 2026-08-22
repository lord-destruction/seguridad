import base64, codecs, sys

rot13Str = "mVGZ3O3omkJLmy2pcuTq"
base64Str = codecs.decode(rot13Str[::-1], 'rot13')
clearTextStr = base64.b64decode(base64Str)
print (clearTextStr)
