import tempfile

class DNAComparison:
    def __init__(self, body_file, parents_file, output_file):
        self.body_file = body_file
        self.parents_file = parents_file
        self.output_file = output_file

    def compare_dna(self):
        with tempfile.TemporaryFile() as body_file_temp, \
             tempfile.TemporaryFile() as parents_file_temp, \
             tempfile.TemporaryFile() as output_file_temp:
            # Save the body file to a temporary file
            body_file_temp.write(self.body_file.read())
            body_file_temp.seek(0)

            # Save the parents file to a temporary file
            parents_file_temp.write(self.parents_file.read())
            parents_file_temp.seek(0)

            # Call the DNAComparison class
            dna_comparison = DNAComparison(body_file_temp, parents_file_temp, output_file_temp)
            dna_comparison.compare_dna()

            # Read the output file and return the response
            output_file_temp.seek(0)
            response = HttpResponse(output_file_temp.read(), content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename=output.txt'

        return response