#----------------------------------------------------------------------------------------
# T R I E  S E A R C H E R  -  P R E F I X  +  S U F F I X
#----------------------------------------------------------------------------------------
# Use case : grab all keywords per account
# Logic flow: Search trie for prefix (account id), then capture all suffix (keywords).
#----------------------------------------------------------------------------------------

import ast
from trie import Trie

def load_trie_file(aTrie, aFile):                            # Load trie (from a file) into memory
    with open(aFile, "r") as f:                              # Open a previously persisted trie
        for line in f.readlines():
            lineStripped = line.strip()                      #just in case, strip leading spaces, trailing spaces and crlf
            aTrie.child = ast.literal_eval(lineStripped)     # convert a line of string to dict then load into trie
    return aTrie

def list_words(t):                        # t is a dictionary. return a list.
    my_list = []
    for k, v in t.items():
        if k != '#':
            for el in list_words(v):
                my_list.append(k + el)
        else:
            my_list.append("")
    return my_list


def main():                                              

    trie_obj = Trie()                                # Instantiate a new Trie object

    f_trie = "data/trie_02.txt"                          # Persisted trie
    prefix = "zigz"                                  # Prefix (or account id for the sample use case)

    trie_obj = Trie()                                # Create a Trie object
    trie_obj = load_trie_file(trie_obj, f_trie)      # Load trie object with previously persisted trie file
    
    sub_trie = trie_obj.child

    for letter in prefix:             
        sub_trie = sub_trie[letter]                  # k:v. On k, save the v (also a dictionary). Then do again until no more.

    print('\n----- Summary -----')
    print(type(sub_trie))              # for tech reference only
    print(sub_trie)                    # for tech reference only
    print(list_words(sub_trie))        # This is the desired result. All the suffixes matching the prefix.
    print(type(list_words(sub_trie)))  # for tech reference only
    print('----- End -----\n')


if __name__ == "__main__":
    main()
