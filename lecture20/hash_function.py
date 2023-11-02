from hashlib import sha1

print(sha1("hello world".encode('utf-8')).hexdigest())
print(sha1("short".encode('utf-8')).hexdigest())
long_str = """
This is a reaaaaaaaaaalllllllllyyyyyyy loooooonnnngggg 
sssstttrrrriiinnngggg.  It doesn't say anything important.
It just goes on an on.
"""
print(sha1(long_str.encode('utf-8')).hexdigest())