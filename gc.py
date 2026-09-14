def calc_gc(sequence: str) -> float:
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100.0

def highest_gc(file_path: str) -> tuple[str, float]:
    with open(file_path, "r") as file:
        dataset = file.read().strip().split(">")[1:]

    max_gc = 0.0;
    max_id = ""

    for chunk in dataset:
        lines = chunk.strip().splitlines()
        id = lines[0]
        sequence = "".join(lines[1:]).replace(" ", "").upper()
        curr_gc = calc_gc(sequence)
        if curr_gc > max_gc:
            max_gc = curr_gc
            max_id = id

    return (max_id, max_gc)

if __name__ == "__main__":
    dataset_file = "data/rosalind_gc.txt"
    try:
        fasta_id, gc_content = highest_gc(dataset_file)
        print(f"{fasta_id}\n{gc_content:.6f}")
    except FileNotFoundError:
        print(f"Could not find file {dataset_file}. Check file path!")
