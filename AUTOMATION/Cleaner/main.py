from Cleaner import Clean


img = Clean(('.png', 'jpg', 'icon'), 'images')
doc = Clean(('.epub', 'pdf', 'txt'), 'documents')
arc = Clean(('zip', '.rar'), 'archievs')
vid = Clean(('.mp4', '.avi'), 'videos')

if __name__ == '__main__':
    img.arrange()
    doc.arrange()
    arc.arrange()
    vid.arrange()