#----------------------------------------------------------------------------------
# T R I E  B U I L D E R
#----------------------------------------------------------------------------------
# This trie example builds the following dictionary:
#   trie_obj.child = {'r': {'e': {'a': {'d': {'#': 1}}, 's': {'t': {'#': 1}}}}}
#----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------
# To Dos:
# 1. Trie structure #1 : Use keywords as first part of trie followed by user id. So every keyword has userid tail ends.
#       1.1 Search for keyword (prefix) and return all userids (suffix).
# 2. Trie structure #2 : Use userid as first part of trie followed by keywords. T
#       2.1 This keeps track of user's keywords.
#       2.2 Can be used as initial storage for user data, then gets converted later on to trie structure #1.
# 3. How can this work with encrypted data?
# 4. Combine two tries. Is there a use case for this?
#----------------------------------------------------------------------------------

import ast                                                  # Abstract Syntax Trees
from trie import Trie                                       # Trie class

def load_trie_file(aTrie, aFile):                           # Load trie (from a file) into memory
    with open(aFile, "r") as f:                             # Open a previously persisted trie
        for line in f.readlines():                          # Process each line/word
            lineStripped = line.strip()                     # Just in case, strip leading spaces, trailing spaces and crlf
            aTrie.child = ast.literal_eval(lineStripped)    # Convert a line of string to dict then load into trie
    return aTrie

def add_new_data_into_trie(aTrie, aFile):                   # Add new data/interests into trie (in memory)
    with open(aFile, "r") as f:                             # New interests data
        for line in f.readlines():                          # Process each line/word
            lineStripped = line.strip()                     # Just in case, strip leading spaces, trailing spaces and crlf.
            aTrie.insert(lineStripped)                      # Insert word into trie
    return aTrie

def write_new_trie_file(aTrie, aFile):                      # Write trie (in memory) into file (in trie dictionary structure)
    f = open(aFile, "x")                                    # create a new file; error if file already exists
    f.write(str(aTrie.child))                               # write trie data dictionary into a new file
    f.close()                                               # close file

def main():                                                 # This is the main routine, execution begins here.
    print("-----------------------------")
    print("Trie Builder starting up...")

    f_trie_old = "data/trie_01.txt"
    f_keywords = "data/word_list.txt"
    f_trie_new = "data/trie_new_01.txt"

    trie_obj = Trie()                                        # Create a Trie object
    trie_obj = load_trie_file(trie_obj, f_trie_old)          # Load trie object with previously persisted trie file
    trie_obj = add_new_data_into_trie(trie_obj, f_keywords)  # Add new user interests into trie object
    write_new_trie_file(trie_obj, f_trie_new)                # Write updated trie to a new file.

    print("f_trie_old = " + f_trie_old)
    print("f_keywords = " + f_keywords)
    print("f_trie_new = " + f_trie_new)
    print("Trie Builder ending.")
    print("-----------------------------")


if __name__ == "__main__":
    main()
