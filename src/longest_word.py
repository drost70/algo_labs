def longest_word(words):
    if not words:
        return 0
    words.sort(key=len)

    dp = [1] * len(words)

    for i in range(len(words)):
        for j in range(i):
            if is_one_letter_less(words[i], words[j]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def is_one_letter_less(word1, word2):
    if len(word1) != len(word2) + 1:
        return False

    for i in range(len(word2)):
        if word1[i] != word2[i]:
            return word1[i + 1:] == word2[i:]

    return True


if __name__ == "__main__":
    with open("./src/wchain.in", "r") as file_in, open("./src/wchain.out", "w") as file_out:
        N = int(file_in.readline().strip())
        words = [file_in.readline().strip() for _ in range(N)]

        result = longest_word(words)
        file_out.write(str(result))
