class Trie:
    """
    A class that represents the Trie data structure
    """
    def __init__(self):
        self.child = {}


    def insert(self, word):
        """Inserts a word into the trie

        Parameter
        ---------
        word : str
            This is the word that gets pushed into the trie
        """
        current = self.child

        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]

        current["#"] = 1


    def search(self, word):
        """Determines whether a word exists inside the trie

        Parameters
        -------
        word : str
            The word that is checked
        Returns
        -------
        bool
            True if the word exists in side the trie, False otherwise
        """
        current = self.child

        for c in word:
            if c not in current:
                return False
            current = current[c]

        return "#" in current


    def starts_with(self, prefix):
        """Checks if a prefix is in the trie

        A prefix is a string of characters. It exists in a trie if a
        word begins with the prefix, or if the prefix itself is a word.

        Parameters
        ----------
        prefix : str
            This is the prefix that is checked
        Returns
        -------
        bool
            True if the prefix exists in the trie, False otherwise
        """
        current = self.child

        for c in prefix:
            if c not in current:
                return False
            current = current[c]

        return True
