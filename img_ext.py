import os, glob
import io
import fitz
from PIL import Image

path = 'C:/Users/user/Desktop/BV/lala/'

for infile in glob.glob(os.path.join(path, '*.pdf')):
    pdf_file = fitz.open(infile)
    
    for page_index in range(len(pdf_file)) :
        page = pdf_file[page_index]
        image_list = page.get_images()

        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else: 
            print("[!]No images found on page", page_index)
        for image_index, img in enumerate(page.get_images(), start=1):
            xref = img[0]
            
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            
            image_ext = base_image["ext"]
            
            image = Image.open(io.BytesIO(image_bytes))
            if image.height >= 100 and image.width >= 100:
                image.save(open(f"{infile}{image_index}.{image_ext}", "wb"))