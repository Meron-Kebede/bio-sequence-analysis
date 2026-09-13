def num_of_rabbits(file_path: str) -> int:
    with open(file_path, "r") as file:
        input = file.read().strip().split()
        n, k = int(input[0]), int(input[1])
    if n <= 2:
        return 1
    f1, f2 = 1, 1
    for _ in range(3, n+1):
        f1, f2 = f2, f2 + (k*f1)
    return f2

if __name__ == "__main__":
    dataset_file = "data/rosalind_fib.txt"
    try:
        print(num_of_rabbits(dataset_file))
    except FileNotFoundError:
        print(f"Could not find file {dataset_file}. Check file path!")