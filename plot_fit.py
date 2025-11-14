import math 
import matplotlib.pyplot as plt 

def plot_fit(algorithm_name, n_values, t_values, regression_result):
    n = [float(v) for v in n_values]
    t = [float(v) for v in t_values]

    # Prepare transformed x-values
    X_linear = [ni for ni in n]
    X_nlogn  = [ni * math.log2(ni) for ni in n]
    X_n2     = [ni ** 2 for ni in n]

    # Compute fitted curves for each model
    # y(n) = beta0 + beta1 * X(n)
    b0_lin = regression_result["O(n)"]["beta0"]
    b1_lin = regression_result["O(n)"]["beta1"]
    y_lin  = [b0_lin + b1_lin * x for x in X_linear]

    b0_nl  = regression_result["O(n log n)"]["beta0"] 
    b1_nl  = regression_result["O(n log n)"]["beta1"]
    y_nlog = [b0_nl + b1_nl * x for x in X_nlogn]

    b0_q   = regression_result["O(n^2)"]["beta0"]
    b1_q   = regression_result["O(n^2)"]["beta1"]
    y_quad = [b0_q + b1_q * x for x in X_n2]

    # Plot
    plt.figure(figsize=(9, 6))
    plt.scatter(n, t, label="Measured data", s=40)

    plt.plot(n, y_lin,  label="O(n) fit")
    plt.plot(n, y_nlog, label="O(n log n) fit")
    plt.plot(n, y_quad, label="O(n^2) fit")

    plt.title(f"Complexity model fits for {algorithm_name}")
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()