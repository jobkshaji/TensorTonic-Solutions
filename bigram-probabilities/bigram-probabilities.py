from collections import defaultdict
def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    vocab=set(tokens)
    V=len(vocab)

    counts=defaultdict(int)
    unigram=defaultdict(int)

    for i in range(len(tokens)-1):
      w1,w2=tokens[i],tokens[i+1]
      counts[(w1,w2)]+=1
      unigram[(w1)]+=1
    
    probs={}
    for w1 in vocab:
      denominator=unigram[w1]+V
      for w2 in vocab:
        c=counts.get((w1,w2),0)
        probs[(w1,w2)]=(c+1)/denominator
    # Your code here
    return dict(counts),probs