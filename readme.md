Let's break down the code and its purpose in a simple way:

### Code Explanation

#### Imports and Function Definitions

```python
import hashlib
```
- This line imports the `hashlib` library, which provides implementations of hashing algorithms like SHA-256.

```python
def hash_words(word):
    return hashlib.sha256(word.encode()).hexdigest()
```
- `hash_words(word)`: This function takes a `word` as input, converts it to its SHA-256 hash using `hashlib.sha256()`, encodes it as bytes, and then returns the hexadecimal representation of the hash using `.hexdigest()`.

#### Brute Force Function

```python
def brute_force(wordlist_file, hash_file):
    with open(wordlist_file, "r") as file:
        wordlist = [line.strip() for line in file]
    with open(hash_file, "r") as file:
        hashes = {line.strip() for line in file}

    found_values = {}

    for word in wordlist:
        word_hash = hash_words(word)
        if word_hash in hashes:
            found_values[word_hash] = word
            print(f"{word} -> {word_hash}")

    if not found_values:
        print("No hashes were found")
    else:
        print("\nMatched hashes:")
        for h, w in found_values.items():
            print(f"{h}: {w}")
```
- `brute_force(wordlist_file, hash_file)`: This function performs a brute-force search to find matches between words in `wordlist_file` and hashes in `hash_file`.

#### Detailed Steps

1. **Reading Files**:
   - `wordlist_file` contains a list of words that we want to hash and check against the hashes in `hash_file`.
   - `hash_file` contains a list of precomputed SHA-256 hashes (one per line), which we want to match with words in `wordlist_file`.

2. **Processing Word List**:
   - The `wordlist` variable is created by reading `wordlist_file` line by line and stripping any extra whitespace characters (like newline characters `\n`).

3. **Processing Hashes**:
   - The `hashes` set is created similarly by reading `hash_file` line by line and stripping whitespace characters.

4. **Brute Force Matching**:
   - The code iterates over each word in `wordlist`.
   - For each word, it computes its SHA-256 hash using the `hash_words()` function.
   - It then checks if this computed hash exists in the `hashes` set.
   - If a match is found, it stores the hash-value pair in `found_values` and prints the word and its corresponding hash.

5. **Output**:
   - If no matches are found (`found_values` is empty), it prints "No hashes were found".
   - Otherwise, it prints all matched hashes and their corresponding words.

### Simplified Explanation

The program reads a list of words from `wordlist_file` and a set of SHA-256 hashes from `hash_file`. It then computes the SHA-256 hash for each word and checks if the hash exists in the set of precomputed hashes. If a match is found, it prints the word and its hash. If no matches are found, it notifies the user accordingly.

This type of program is often used in scenarios like password cracking or verifying the integrity of data against known hashes. It demonstrates the basic usage of cryptographic hashing and file operations in Python.