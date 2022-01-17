from trie import Trie


class style:
    """A small class for text styling in print statements"""
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def main():
    """This function runs when this file is ran as the main file."""

    # Creating a Trie object
    trie_obj = Trie()

    print(style.BOLD + style.UNDERLINE + "\nINSERTIONS\n" + style.END)

    # Inserting words into the trie
    print("Inserting 'read' into the trie.\n")
    trie_obj.insert("read")

    print("Inserting 'rest' into the trie.")
    trie_obj.insert("rest")

    print(style.BOLD + style.UNDERLINE + "\n\nSEARCHES\n" + style.END)

    # Checking if words exist in the trie
    print("Checking if 'read' is in the trie:")
    print(trie_obj.search("read"))

    print("\nChecking if 'rest' is in the trie:")
    print(trie_obj.search("rest"))

    print("\nChecking if 'python' is in the trie:")
    print(trie_obj.search("python"))

    print("\nChecking if 'reel' is in the trie:")
    print(trie_obj.search("reel"))


    print(style.BOLD + style.UNDERLINE + "\n\nPREFIXES\n" + style.END)

    # Checking if prefixes exist in the trie
    print("Checking if 're' is a prefix in the trie:")
    print(trie_obj.starts_with("re"))

    print("\nChecking if 'py' is a prefix in the trie:")
    print(trie_obj.starts_with("py"))



if __name__ == "__main__":
    main()
