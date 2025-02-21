from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Counts the number of words in the Trie that end with the given suffix (pattern).

        Args:
            pattern (str): The suffix to search for.

        Returns:
            int: The number of words ending with the given suffix.
        """
        if not isinstance(pattern, str) or not pattern:
            raise ValueError("Pattern must be a non-empty string")

        count = 0
        for word in self.keys():
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix: str) -> bool:
        """
        Checks if there is at least one word in the Trie that starts with the given prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if at least one word starts with the given prefix, otherwise False.
        """
        if not isinstance(prefix, str) or not prefix:
            raise ValueError("Prefix must be a non-empty string")

        return any(word.startswith(prefix) for word in self.keys())


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Check suffix count
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Check prefix presence
    assert trie.has_prefix("app") is True  # apple, application
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True  # banana
    assert trie.has_prefix("ca") is True  # cat

    print("All tests passed successfully!")
