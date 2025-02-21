from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        """
        Finds the longest common prefix among a list of strings.

        Args:
            strings (List[str]): List of words.

        Returns:
            str: The longest common prefix, or an empty string if there is none.
        """
        if not strings:
            return ""

        # Insert all words into Trie
        for word in strings:
            self.put(word, True)

        # Find the longest common prefix
        prefix = []
        node = self.root
        while (
            node and len(node.children) == 1 and node.value is None
        ):  # Ensure it's a prefix
            char = next(iter(node.children))  # Get the only character
            prefix.append(char)
            node = node.children[char]

        return "".join(prefix)


if __name__ == "__main__":
    # Tests
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed successfully.")
