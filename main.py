from linear_regression import analyze_complexity, best_complexity_model

def parse_list(input_list):
    numbers = input_list.split(",")
    values = []
    for number in numbers:
        values.append(float(number))
    return values 

def main():
    print("Welcome to ComplexiFit!")
    print("An empirical complexity regression tool.")

    algorithm_name = input("Name of the algorithm: ")
    if not algorithm_name: 
        algorithm_name = "Unnamed algorithm"
    
    print(f"\nInput sizes n for {algorithm_name}.")
    print("It has to be in the format below (comma seperated numbers)")
    n_val = input("Input n here: ")
    n_values = parse_list(n_val)

    print(f"\nInput running times t for {algorithm_name}.")
    print("It has to be in the format below (comma seperated numbers)")
    t_val = input("Input t here: ")
    t_values = parse_list(t_val)

    results = analyze_complexity(n_values, t_values)

    best_model, best_R2 = best_complexity_model(results)

    # print 3 decimals
    print(f"\nRegression results for {algorithm_name}:")
    print(f"\nO(n):       R^2 = {results["O(n)"]["R2"]:.3f}")
    print(f"O(n log n): R^2 = {results["O(n log n)"]["R2"]:.3f}")
    print(f"O(n^2):     R^2 = {results["O(n^2)"]["R2"]:.3f}")
    print(f"\nBest fit:   {best_model}")

if __name__ == "__main__":
    main()

