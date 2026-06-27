import hashlib
import requests

# Check if the given password has been exposed in a data breach using the Have I Been Pwned API
def check_breach(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper() # Compute the SHA-1 hash of the password and convert it to uppercase

    prefix = sha1_hash[:5] # Get the first 5 characters of the hash to use as a prefix for the API request
    suffix = sha1_hash[5:] # Get the remaining characters of the hash to use as a suffix for comparison with the API response

    url = f"https://api.pwnedpasswords.com/range/{prefix}" # Construct the URL for the Have I Been Pwned API using the prefix

    response = requests.get(url) # Send a GET request to the API to retrieve the list of hashes that match the prefix
     
     # Check if the response status code is not 200 (OK). If it's not, return None to indicate that the breach check failed.
    if response.status_code != 200:
        return None
    
    # Split the response text into lines, where each line contains a hash suffix and the count of how many times that password has been seen in breaches. The format is "hash_suffix:count".
    hashes = response.text.splitlines()

    # Iterate through each line in the response
    for line in hashes:
        hash_suffix, count = line.split(":")

        if hash_suffix == suffix:
            return int(count)

    return 0