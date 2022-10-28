#a script that converts images to pdf

from reportlab.platypus import Image, SimpleDocTemplate


def images_to_pdf(
    list_of_images: list, pdf_file_name: str, width=None, height=None, hAlign="CENTER"
) -> bool:
    """
    Function convert the image into Pdf
    """
    pdf = SimpleDocTemplate(pdf_file_name)
    images = []
    for i in list_of_images:
        try:
            re = Image(i, width=width, height=height, hAlign=hAlign)
        except:
            pass
        images.append(re)
    pdf.build(images)

    return True


if __name__ == "__main__":
    # You Can use any source of image
    # Here I use posts of Instagram with hashtag 'tamil'
    from instagramy import InstagramHashTag

    tag = InstagramHashTag("tamil")
    print(images_to_pdf(tag.posts_display_urls, "tamil.pdf", width=250, height=250))
