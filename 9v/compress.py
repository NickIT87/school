import zipfile


def compress_file(input_filename, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_filename, arcname=input_filename)


def extract_zip(zip_filename, extract_path):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


input_filename = 'a.out'
output_filename = 'compressed.zip'
zip_filename = 'compressed.zip'
extract_path = 'extracted/'


compress_file(input_filename, output_filename)
extract_zip(zip_filename, extract_path)