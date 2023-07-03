# کد کلاس DNAComparison و مثال استفاده از آن

class DNAComparison:
    def __init__(self, body_file, parents_file, output_file):
        self.body_file = body_file
        self.parents_file = parents_file
        self.output_file = output_file

    def compare_dna(self):
        with open(self.body_file, 'r') as body_file, \
             open(self.parents_file, 'r') as parents_file, \
             open(self.output_file, 'w') as output_file:
            body_dna = body_file.readline().strip()
            for line in parents_file:
                parent_dna = line.strip()
                similarity, common_chars = self.calculate_similarity(body_dna, parent_dna)
                output_line = f"{body_dna}\t{parent_dna}\t{similarity}\t{common_chars}\n"
                output_file.write(output_line)

    def calculate_similarity(self, dna1, dna2):
        common_chars = ""
        similarity = 0
        for base1, base2 in zip(dna1, dna2):
            if base1 == base2:
                similarity += 1
                common_chars += base1
        return similarity, common_chars


# مثال استفاده از کلاس

dna_comparison = DNAComparison('dna_body.txt', 'dna_parents.txt', 'output.txt')
dna_comparison.compare_dna()
