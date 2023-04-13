from PIL import Image, ImageFilter

img = Image.open('processed_image.jpg')
denoised_img = img.filter(ImageFilter.MedianFilter(size=3))
denoised_img.save('denoised_image.jpg')
