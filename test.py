import post_creator as pc

with open('texts.txt', mode='r', encoding='utf-8') as text_file:
    texts = text_file.readlines()
for x, text in enumerate(texts):
    img = pc.create_content(img_path= 'images/'+str(x+1)+'.jpg', text=text, text_color=(255, 255, 255), text_background_color=(255, 0, 0, 50), text_font='BebasNeue-Regular.ttf', pos='story')
    img.save('images/'+str(x+1)+'_new.jpg')