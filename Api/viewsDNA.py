import tempfile
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def upload_files(request):
    body_file = request.FILES.get('body_file')
    parents_file = request.FILES.get('parents_file')

    # Save the uploaded files to temporary files
    with tempfile.TemporaryFile() as body_file_temp, \
            tempfile.TemporaryFile() as parents_file_temp:
        body_file_temp.write(body_file.read())
        body_file_temp.seek(0)
        parents_file_temp.write(parents_file.read())
        parents_file_temp.seek(0)

        # Return success response
        return HttpResponse(status=201)


@api_view(['POST'])
def compare_dna(request):
    body_file = request.FILES.get('body_file')
    parents_file = request.FILES.get('parents_file')

    # Save the uploaded files to temporary files
    with tempfile.TemporaryFile() as body_file_temp, \
            tempfile.TemporaryFile() as parents_file_temp:

        body_file_temp.write(body_file.read())
        body_file_temp.seek(0)
        parents_file_temp.write(parents_file.read())
        parents_file_temp.seek(0)

        # Read the DNA sequences from the input files
        body_dna = body_file_temp.read().decode("utf-8").strip()
        parents_dna = parents_file_temp.read().decode("utf-8").strip().split("\n")

        # Compare the DNA sequences and find the similarities
        similarities = []
        for parent_dna in parents_dna:
            for i in range(len(body_dna)):
                if body_dna[i:i + len(parent_dna)] == parent_dna:
                    similarities.append((i, parent_dna))

        # Format the output as a TSV file
        output_file_temp = tempfile.TemporaryFile(mode='w+', encoding='utf-8')
        for similarity in similarities:
            output_file_temp.write(
                f"{body_dna[similarity[0]:similarity[0] + len(similarity[1])]}\t{similarity[1]}\n")
        output_file_temp.seek(0)

        # Return the output file as a response
        response = HttpResponse(output_file_temp.read(), content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=output.tsv'

        return response
