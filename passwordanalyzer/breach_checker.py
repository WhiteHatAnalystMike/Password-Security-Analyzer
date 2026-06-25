import hashlib
import requests


def check_breach(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")

        if hash_suffix == suffix:
            return int(count)

    return 0