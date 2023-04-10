import numpy as np


# Define Cost functions
def sub_cost(l1: str, l2: str) -> float:
    """
    Compute the substitution cost between two letters l1 and l2.

    Args:
        l1: A letter from the alphabet Σ
        l2: A letter from the alphabet Σ

    Returns:
        The substitution cost between l1 and l2.
    """
    if l1 == l2:
        return 0
    elif l1.lower() == l2.lower():
        return 1
    else:
        return 2


def sed(string1: str, string2: str) -> float:
    """
    Compute the string edit distance between the two given strings.

    Args:
        string1: A string sequence
        string2: A string sequence

    Returns:
        String edit distance between the two input strings.
    """
    m, n = len(string1), len(string2)
    D = np.zeros((m + 1, n + 1), dtype=int)

    # Initialize the first row and column of the cost matrix
    for i in range(m + 1):
        D[i, 0] = i
    for j in range(n + 1):
        D[0, j] = j

    # Compute the cost matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            deletion_cost = D[i - 1, j] + 1
            insertion_cost = D[i, j - 1] + 1
            substitution_cost = D[i - 1, j - 1] + sub_cost(
                string1[i - 1], string2[j - 1]
            )
            D[i, j] = min(deletion_cost, insertion_cost, substitution_cost)

    return D[m, n]


def main():
    # Load list of words/texts to compare from 'data/texts.txt'
    with open("data/texts.txt", "r") as file:
        texts = file.readlines()

    # Clean and split the words
    words = [text.strip() for text in texts]

    # Compute the string edit distance between all pairs of loaded words
    GEDs = np.zeros((len(words), len(words)), dtype=int)
    for i in range(len(words)):
        for j in range(i, len(words)):
            GEDs[i, j] = GEDs[j, i] = sed(words[i], words[j])

    # Save the GEDs in './results/SED_results.csv'
    np.savetxt("./results/SED_results.csv", GEDs, fmt="%i", delimiter=",")


if __name__ == "__main__":
    main()
