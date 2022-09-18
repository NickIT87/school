# import zipfile
# jungle_zip = zipfile.ZipFile('my_next.zip', 'w')
# jungle_zip.write('test.txt', compress_type=zipfile.ZIP_DEFLATED)
# jungle_zip.close()


# import zipfile
# fantasy_zip = zipfile.ZipFile('my.zip')
# fantasy_zip.extractall('')
# fantasy_zip.close()

import zipfile
jungle_zip = zipfile.ZipFile('my_img.zip', 'w')
jungle_zip.write('img.png', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()
