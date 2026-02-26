def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    import numpy as np
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    classes=np.unique(np.concatenate([y_true, y_pred]))

    tp=fp=fn=0
    for c in classes:
        tp += np.sum((y_true == c) & (y_pred == c))
        fp += np.sum((y_true != c) & (y_pred == c))
        fn += np.sum((y_true == c) & (y_pred != c))

    if tp == 0:
        return 0.0

    precision = tp / (tp + fp)
    recall    = tp / (tp + fn)

    return 2 * precision * recall / (precision + recall)