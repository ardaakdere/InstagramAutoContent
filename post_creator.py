from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os

path = os.path.dirname(__file__)
os.chdir(path)

story_sizes = [(1080*x, 1920*x) for x in range(1,11)]

def get_proper_res(img, which = 'story'):
    w, h = img.size
    resolution = (0 ,0)
    if which == 'story':
        for size in story_sizes:
            if size[0] <= w and size[1] <= h:
                resolution = (size[0], size[1])
    elif which == 'post':
        min_ = min(w, h)
        resolution = (min_, min_)
    return resolution

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                        (img_height - crop_height) // 2,
                        (img_width + crop_width) // 2,
                        (img_height + crop_height) // 2))

def create_content(img_path, text = '', text_font = 'Arial.ttf', text_color = (255, 255, 255), text_background_color = (0, 0, 0, 0), blur = 15, pos = 'story'):
    img = Image.open(img_path)

    img2 = img.filter(ImageFilter.GaussianBlur(blur))

    prop_res = get_proper_res(img2, pos)
    print(prop_res)

    img2 = crop_center(img2, prop_res[0], prop_res[1])

    width, height = img2.size

    if pos == 'post':
        font_size = int(width/15)
    elif pos == 'story':
        font_size = int(width/15)

    myFont = ImageFont.truetype(text_font, font_size)

    texts = text.split(' ')
    indent = len(texts)//3
    if indent != 1:
        for b in range(indent):
            if b == indent-1 and indent > 0:
                continue
            texts.insert(3+b*4, '\n')
    text = " ".join(texts)

    d1 = ImageDraw.Draw(img2, mode='RGBA')

    w, h = d1.textsize(text, myFont)

    x_start = (width - w) / 2
    y_start = (height - h) / 2
    d1.rectangle((x_start, y_start, x_start + w, y_start + h), fill=text_background_color)

    texts = text.split('\n')

    for x in texts:
        d1.text((width/2, y_start+font_size), x, fill = text_color, font = myFont, anchor = 'ms')
        y_start += font_size*1.1

    return img2
