import math 

# Simple linear regression
def linear_regression(x, y):
    
    n = len(x)
    
    # Means
    x_bar = sum(x) / n 
    y_bar = sum(y) / n 

    S_xx = sum((xi - x_bar) ** 2 for xi in x)
    S_xy = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y))
    S_yy = sum((yi - y_bar) ** 2 for yi in y)

    beta_1 = S_xy / S_xx 
    beta_0 = y_bar - beta_1 * x_bar 

    y_hat = [beta_0 + beta_1 * xi for xi in x]

    q_0 = sum((yi -yhi) ** 2 for yi, yhi in zip (y, y_hat))

    r_squared = 1 - q_0 / S_yy 

    return beta_0, beta_1, y_hat, r_squared 

def analyze_complexity(n_values, t_values):
    
    # TODO Add the entire hierarchy of complexities
    
    n = [float(v) for v in n_values]
    t = [float(v) for v in t_values]

    X_linear = [ni for ni in n]
    X_nlogn  = [ni * math.log2(ni) for ni in n]
    X_n2     = [ni ** 2 for ni in n]

    b0_lin, b1_lin, _, R2_lin   = linear_regression(X_linear, t)
    b0_nl,  b1_nl,  _, R2_nlog  = linear_regression(X_nlogn,  t)
    b0_q,   b1_q,   _, R2_quad  = linear_regression(X_n2,     t)

    results = {
        "O(n)":       {"beta0": b0_lin, "beta1": b1_lin, "r2": R2_lin},
        "O(n log n)": {"beta0": b0_nl,  "beta1": b1_nl,  "r2": R2_nlog},
        "O(n^2)":     {"beta0": b0_q,   "beta1": b1_q,   "r2": R2_quad},
    }

    return results

def best_complexity_model(results):
    """
    Given the results dictionary from analyze_complexity(),
    return (best_model_name, best_R2_value).
    """
    best_model, best_R2 = max(
        ((name, info["r2"]) for name, info in results.items()),
        key=lambda x: x[1]
    )
    return best_model, best_R2
