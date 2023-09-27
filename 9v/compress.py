# підключення бібліотеки для архівування даних
import zipfile

# функція яка виконує архівування файлу
def compress_file(input_filename, output_filename):
    # оператор контексту який створює програмний об'єкт та записує його в файл
    #with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    #with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_BZIP2) as zipf:
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_LZMA) as zipf:
        # створити архів даних та записати його на диск
        zipf.write(input_filename, arcname=input_filename)

# розпаковка інсуючого архіву
# def extract_zip(zip_filename, extract_path):
#     with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
#         zip_ref.extractall(extract_path)


input_filename = 'a.out'
output_filename = 'compressed.zip'
zip_filename = 'compressed.zip'
extract_path = 'extracted/'


compress_file(input_filename, output_filename)
#extract_zip(zip_filename, extract_path)