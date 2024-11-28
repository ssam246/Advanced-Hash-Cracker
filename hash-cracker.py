import hashlib
import gzip
from optparse import OptionParser
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def generate_hash(content, hash_algorithm):
    """Generates a hash for the given content using the specified algorithm."""
    try:
        hash_instance = hashlib.new(hash_algorithm)
        hash_instance.update(content.encode('utf-8'))
        return hash_instance.hexdigest()
    except ValueError as e:
        print(f"Error: Unsupported hash type {hash_algorithm}.")
        raise e

def get_supported_hash_types():
    """Returns the list of hash algorithms supported by the hashlib library."""
    return hashlib.algorithms_guaranteed

def read_wordlist(file_path):
    """
    Reads a wordlist file. Supports plaintext and compressed files (.gz).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Wordlist file '{file_path}' does not exist.")

    if file_path.endswith(".gz"):
        with gzip.open(file_path, 'rt', encoding="utf-8") as file:
            for line in file:
                yield line.strip("\n")
    else:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                yield line.strip("\n")

def crack_hash(hash_value, hash_type, wordlist_path, multithreading=False):
    """
    Attempts to crack the given hash using the specified wordlist.
    Supports optional multithreading for improved performance.
    """
    wordlist = read_wordlist(wordlist_path)
    found = [False]  # A mutable container to signal when the hash is cracked.

    def test_word(word):
        if found[0]:  # Stop if the hash is already found.
            return
        calculated_hash = generate_hash(word, hash_type)
        if hash_value == calculated_hash:
            print(f"\nHash Found: [ {calculated_hash} ] >> Word: [ {word} ]")
            found[0] = True

    if multithreading:
        with ThreadPoolExecutor() as executor:
            list(tqdm(executor.map(test_word, wordlist), desc="Testing", unit="words"))
    else:
        for word in tqdm(wordlist, desc="Testing", unit="words"):
            test_word(word)
            if found[0]:
                break

    if not found[0]:
        print("\n\tHash not found :(\n")

def main():
    """Main function to parse arguments and execute the hash cracker."""
    usage = """
# Usage:
    python hash_cracker.py --hashvalue <hash_value> --hashtype <hash_type> --wordlist <path_to_wordlist> [--multithread]
# Example:
    python hash_cracker.py --hashvalue 7052cad6b415f4272c1986aa9a50a7c3 --hashtype md5 --wordlist words.txt
    python hash_cracker.py --hashvalue 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed --hashtype sha1 --wordlist words.gz --multithread
"""
    opt_handler = OptionParser(usage)
    opt_handler.add_option("--hashvalue", dest="hash_value", type="string", help="Hash value to be cracked")
    opt_handler.add_option("--hashtype", dest="hash_type", type="string", help="Type of hash: md5, sha1, sha256, etc.")
    opt_handler.add_option("--wordlist", dest="wordlist_path", type="string", help="Path to wordlist file")
    opt_handler.add_option("--multithread", action="store_true", dest="multithreading", default=False, help="Enable multithreaded cracking (optional)")

    (opts, args_list) = opt_handler.parse_args()

    if not (opts.hash_value and opts.hash_type and opts.wordlist_path):
        print(opt_handler.usage)
        exit(1)

    if opts.hash_type not in get_supported_hash_types():
        print(f"Error: Invalid hash type '{opts.hash_type}'.")
        print("Supported hash types are:", ", ".join(get_supported_hash_types()))
        exit(1)

    try:
        crack_hash(opts.hash_value, opts.hash_type, opts.wordlist_path, opts.multithreading)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
