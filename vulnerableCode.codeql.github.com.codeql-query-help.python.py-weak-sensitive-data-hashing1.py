import hashlib

def certificate_matches_known_hash_bad(certificate, known_hash):
    hash = hashlib.md5(certificate).hexdigest() # BAD
    return hash == known_hash