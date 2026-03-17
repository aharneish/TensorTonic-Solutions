def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    
    Args:
        recommended: list of recommended items (ordered)
        relevant: list or set of relevant items
        k: cutoff
    
    Returns:
        (precision_at_k, recall_at_k)
    """
    if k <= 0:
        raise ValueError("k must be > 0")
    
    # Take top-k recommendations
    recommended_k = recommended[:k]
    
    # Convert relevant to set for fast lookup
    relevant_set = set(relevant)
    
    # Count hits
    hits = sum(1 for item in recommended_k if item in relevant_set)
    
    # Precision@k
    precision = hits / k
    
    # Recall@k
    recall = hits / len(relevant_set) if relevant_set else 0.0
    
    return [precision, recall]