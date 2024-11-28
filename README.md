# Advanced Hash Cracker

An advanced designed for brute-forcing cryptographic hashes using a provided wordlist. This tool supports various hash algorithms, provides clear feedback, and offers optional multithreading for improved performance. Created to simplify and enhance your hash-cracking experience.

---

## **Features**
- **Multi-Algorithm Support**: Crack hashes generated with `md5`, `sha1`, `sha256`, and other algorithms supported by Python's `hashlib`.
- **Wordlist Compatibility**: Supports plaintext and compressed wordlist files (`.txt` and `.gz`).
- **Progress Bar**: Visual feedback with progress bars for wordlist testing, powered by `tqdm`.
- **Optional Multithreading**: Boost performance with concurrent wordlist processing.
- **Error Handling**: Informative error messages for unsupported algorithms, invalid inputs, or missing files.
- **User-Friendly CLI**: Simplified command-line interface with intuitive parameters and detailed help.

---

## **Prerequisites**

- Python 3.10.10 installed on your system.
- Required libraries: Install the `tqdm` library for progress bars.
  ```bash
  pip install tqdm
  ```

---

## **Usage**

Run the hash cracker with the following syntax:

```bash
python hash_cracker.py --hashvalue [HASH_VALUE] --hashtype [HASH_TYPE] --wordlist [PATH_TO_WORDLIST] [--multithread]
```

---

## **Parameters**

| Parameter      | Description                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------|
| `--hashvalue`  | The hash string you want to decode.                                                             |
| `--hashtype`   | The algorithm used to encode the hash (e.g., `md5`, `sha1`, `sha256`, etc.).                    |
| `--wordlist`   | Path to the wordlist file you want to use for brute-forcing. Supports `.txt` and `.gz` formats. |
| `--multithread`| (Optional) Enable multithreaded cracking for faster performance.                                |

---

## **Example Commands**

### Crack an MD5 Hash with a Wordlist:
```bash
python hash_cracker.py --hashvalue 7052cad6b415f4272c1986aa9a50a7c3 --hashtype md5 --wordlist words.txt
```

### Crack a SHA1 Hash Using a Compressed Wordlist with Multithreading:
```bash
python hash_cracker.py --hashvalue 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed --hashtype sha1 --wordlist words.gz --multithread
```

---

## **Supported Hash Algorithms**

The tool supports all algorithms provided by Python's `hashlib`. Commonly used options include:
- `md5`
- `sha1`
- `sha224`
- `sha256`
- `sha512`

To view all supported algorithms, run the following in Python:
```python
import hashlib
print(hashlib.algorithms_guaranteed)
```

---

## **Wordlist Compatibility**

This tool supports:
1. **Plaintext Wordlists**: Standard `.txt` files with one word per line.
2. **Compressed Wordlists**: `.gz` files for efficient storage and processing.

---

## **Error Handling**

The tool includes robust error-handling mechanisms:
- **Unsupported Hash Type**: Provides a list of supported hash algorithms if an invalid one is supplied.
- **File Not Found**: Displays a clear error if the specified wordlist is missing.
- **General Errors**: Catches and reports unexpected issues to improve debugging.

---

## **Output Example**

When a match is found:
```text
Testing: 100%|█████████████████████████████████████████| 5000/5000 [00:05<00:00, 890.12 words/s]

Hash Found: [ 7052cad6b415f4272c1986aa9a50a7c3 ] >> Word: [ password123 ]
```

When no match is found:
```text
Testing: 100%|█████████████████████████████████████████| 5000/5000 [00:05<00:00, 890.12 words/s]

	Hash not found :(
```

---

## **Performance Optimization**

### Multithreading
Enable the `--multithread` flag for faster performance on large wordlists. This utilizes Python's `ThreadPoolExecutor` to process multiple words concurrently.

### Example:
```bash
python hash_cracker.py --hashvalue <hash_value> --hashtype sha256 --wordlist large_words.txt --multithread
```

---

## **Contributions**

Feedback and contributions are welcome! Feel free to submit issues or pull requests to enhance this tool.

---

## **Disclaimer**

This tool is intended for educational and ethical purposes only.  
The author does not condone the use of this software for illegal or malicious activities.  
Use responsibly and ensure you have permission to test any hash values.

---

Created with 💻 and 🔐 by **Stephen**.

