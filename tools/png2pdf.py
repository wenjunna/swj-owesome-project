# 导入包
from PIL import Image


def combine_imgs_pdf(img_path_list, pdfFile):
    if len(img_path_list) == 0:
        return False

    png_files = []
    for file in img_path_list:
        if file.endswith(".png"):
            png_files.append(file)

    pdf_poster = Image.open(png_files[0])
    # if pdf_poster.mode == "RGBA":
    pdf_poster = pdf_poster.convert("RGB")
    sources = []
    for file in png_files[1:]:
        png_file = Image.open(file)
        # if png_file.mode == "RGBA":
        png_file = png_file.convert("RGB")
        sources.append(png_file)

    pdf_poster.save(pdfFile, "pdf", save_all=True, append_images=sources)

    return True
