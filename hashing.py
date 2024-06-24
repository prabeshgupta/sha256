#Import library
import hashlib

#SHA-256 (Secure Hash Algorithm 256-bit) produces a hash value (digest) that is 256 bits long, which is equivalent to 32 bytes or 64 hexadecimal characters(4 bits) when represented in hexadecimal format.
def hash_words(word):
    return hashlib.sha256(word.encode()).hexdigest()

def brute_force(wordlist_file, hash_file):
    with open(wordlist_file,"r")as file:
        wordlist = [line.strip() for line in file]
    with open(hash_file,"r")as file:
        hashes = {line.strip() for line in file}

    found_values = {}

    for word in wordlist:
        word_hash  = hash_words(word)
        if word_hash in hashes:
            found_values[word_hash] = word
            print(f" {word} -> {word_hash}")
    
    if not found_values:
            print("No hashes were found")
    else:
            print("\nMatched hashes:")
            for h, w in found_values.items():
                print(f"{h}: {w}")

wordlist_file = "wordlist_file.txt"
hash_file = "hash_file.txt"
    
brute_force(wordlist_file, hash_file)