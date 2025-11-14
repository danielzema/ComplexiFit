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

