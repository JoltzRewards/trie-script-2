# Trie

This project basic implementation of the Trie data structure with example use cases.

## Installation

Download the code through GitHub, or clone this repository.

## Usage

```python
from trie import Trie

# Creates a Trie object
trie_obj = Trie()

# Inserts 'read' into the trie.
trie_obj.insert("read")

# Returns True because 'read' is a word in the trie.
trie_obj.search("read")

# Returns True because 're' is a prefix in the trie.
trie_obj.starts_with("re")
```

## Example Code

Example code is located in `example.py`. Run it using the following command:

```bash
python example.py
```
