from linear_regression import analyze_complexity, best_complexity_model

'''
Program logic: 

We get a bunch of data points from an algorithm: input time (n), runtime (t) for n.

Define: 
C(n) - the time complexity of the algorithm.
f(n) - an "actual complexity", for example log n, n^2 etc.

The goal is to find the f(n) which best suits C(n)

For all the different f(n): 
Plot x = f(n) against y = C(n) and get a curve:
C(n) = a * f(n) + b (where a and b are constants)
We then perform linear regression on the curve and extract the coefficient of determination r^2.

r^2 explains the variance in the data points:
The best candidate of C(n) is the f(n) with the r^2 closest to 1.0.

'''

def parse_list(input_list):
    numbers = input_list.split(",")
    values = []
    for number in numbers:
        values.append(float(number))
    return values 

def main():
    print("\nWelcome to ComplexiFit - an empirical complexity regression tool!")
    print("\nTest your algorithm and gather a set of datapoints.")

    algorithm_name = input("What is the name of the algorithm you used? ")
    if not algorithm_name: 
        algorithm_name = "Unnamed algorithm"
    
    print(f"\nThe input size, n, for {algorithm_name} is needed.")
    print("\nMake sure that delta n is the same for all n")
    print("\n(n can for example be the number of elements in the list you're sorting)")
    print("\nExpected format:")
    print("n: 1,2,3,4,5")
    n_val = input("\nn: ")
    n_values = parse_list(n_val)

    print(f"\nThe last thing needed is the time, t, between each n")
    print("\n(remember that len(n) == len(t))")
    print("\nExpected format:")
    print("\nt: 1,2,3,4,5")
    t_val = input("t: ")
    t_values = parse_list(t_val)

    results = analyze_complexity(n_values, t_values)

    best_model, best_R2 = best_complexity_model(results)

    # print 4 decimals
    print(f"\nRegression results for {algorithm_name}:")
    print(f"\nO(n):       r^2 = {results["O(n)"]["r2"]:.4f}")
    print(f"O(n log n): r^2 = {results["O(n log n)"]["r2"]:.4f}")
    print(f"O(n^2):     r^2 = {results["O(n^2)"]["r2"]:.4f}")
    print(f"\nBest fit:   {best_model}")

if __name__ == "__main__":
    main()

