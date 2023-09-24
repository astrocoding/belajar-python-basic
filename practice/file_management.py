import os
import json

print(os.getcwd())


# contoh JSON:
x = '{"nama":"Zaenal", "umur":20, "kota":"Karawang"}'

# parse x:
y = json.loads(x)

print(y["umur"])