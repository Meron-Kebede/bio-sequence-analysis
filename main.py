
def count_nucleotides(file_path: str) -> dict: 
    with open (file_path, 'r') as file:
        sequence = file.read().strip().upper()
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for char in sequence:
            if char in count:
                count[char] = count[char] + 1
    return count

if __name__ == "__main__":
    dataset_file = "data/rosalind_dna.txt"
    try:
        result = count_nucleotides(dataset_file)
        print(f"{result['A']} {result['C']} {result['G']} {result['T']}")
    except FileNotFoundError:
        print(f"Error: Could not find '{dataset_file}'. Check the file path!")