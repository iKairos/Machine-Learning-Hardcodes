from statistics import mean

def pearsonr(x, y):
    if len(x) != len(y):
        raise ValueError(f"Dataset size is not equal. Size {len(x)} not equal to {len(y)}.")
    
    length = len(x)

    numerator_sum = 0
    term1_sum = 0 
    term2_sum = 0
    
    for i in range(length):
        numerator_sum += (x[i] - mean(x)) * (y[i] - mean(y))

        term1_sum += (x[i] - mean(x)) ** 2
        term2_sum += (y[i] - mean(y)) ** 2
    
    return numerator_sum / (term1_sum * term2_sum) ** 0.5
