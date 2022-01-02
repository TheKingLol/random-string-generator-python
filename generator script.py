import random, string

size = 12
allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
randomstring = ''.join([allowed[random.randint(0, len(allowed) - 1)] for x in xrange(size)])

print randomstring