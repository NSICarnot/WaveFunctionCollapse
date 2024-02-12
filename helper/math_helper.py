import math

def shannon_entropy(probabilities: list[float | int]) -> int:
    entropy = 0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy
