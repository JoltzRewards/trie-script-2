# Trubit's Trie

Trubit customer data in Trie.

## Modules

1. trie - Trie class

2. trie_builder - builds Trie data from a text file

3. trie_searcher - search for prefix keyword

4. trie_searcher_suffix - search for suffix, after matching prefix


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
