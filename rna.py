def transcribe_dna(file_path: str) -> str:
    with open (file_path, 'r') as file:
        sequence = file.read().strip().upper()
    return sequence.replace('T', 'U')

if __name__ == "__main__":
    dataset_file = "data/rosalind_rna.txt"

    try:
        print(transcribe_dna(dataset_file))
    except FileNotFoundError:
        print(f"Could not find '{dataset_file}'. Check the file path!")
