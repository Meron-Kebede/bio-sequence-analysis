def reverse_complement(file_path: str) -> str:
    with open(file_path, 'r') as file:
        sequence = file.read().strip().upper()
    complements = str.maketrans("ATGC", "TACG")
    return sequence.translate(complements)[::-1]

if __name__ == "__main__":
    dataset_file = "data/rosalind_revc.txt"
    try:
        print(reverse_complement(dataset_file))
    except FileNotFoundError:
        print(f"Could not find file '{dataset_file}'. Check the file path!")