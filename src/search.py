def search(haystack, needle):
    comparisons = 0
    last_position = -1

    for i in range(len(haystack) - len(needle) + 1):
        match = all(haystack[i + j] == needle[j] for j in range(len(needle)))
        comparisons += len(needle)

        if match:
            last_position = i

    return last_position, comparisons


text = "abababababab"
search_term = "aba"
final_position, comparison_count = search(text, search_term)
print("Last position:", final_position)
print("Comparisons made:", comparison_count)
