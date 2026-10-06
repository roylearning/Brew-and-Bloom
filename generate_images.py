from PIL import Image, ImageDraw
import os

images_dir = r"C:\Users\royra\OneDrive\Desktop\clade demo\images"

# Hero image
w, h = 460, 613
img = Image.new('RGB', (w, h), '#3E2723')
draw = ImageDraw.Draw(img)
draw.rectangle([138, 370, 322, 377], fill='#D4A373')
draw.rectangle([161, 286, 299, 377], fill='#D4A373')
draw.arc([115, 226, 345, 333], 0, 180, fill='#D4A373', width=4)
img.save(os.path.join(images_dir, 'hero-coffee.png'))
print('hero OK')

# Menu items
menu_items = [
    ('espresso'), ('caramel-latte'), ('cold-brew'), ('affogato'),
    ('capuccino'), ('mocha'), ('earl-grey'), ('matcha-latte'),
    ('croissant'), ('blueberry-muffin'), ('cinnamon-roll'),
]

for name in menu_items:
    w, h = 300, 200
    if 'latte' in name or 'capp' in name:
        bg = '#6F4E37'
    elif 'mocha' in name:
        bg = '#3E2723'
    elif 'cold' in name or 'brew' in name or 'espresso' in name:
        bg = '#6F4E37'
    elif 'affogato' in name:
        bg = '#3E2723'
    elif 'earl' in name or 'matcha' in name:
        bg = '#6F4E37'
    else:
        bg = '#3E2723'
    img = Image.new('RGB', (w, h), bg)
    draw = ImageDraw.Draw(img)
    color = '#D4A373'
    draw.rectangle([w*0.25, h*0.3, w*0.75, h*0.6], fill=color)
    img.save(os.path.join(images_dir, f'{name}.png'))
    print(f'{name} OK')

# Review avatars
for name in ['sarah', 'james', 'amara']:
    w, h = 40, 40
    img = Image.new('RGB', (w, h), '#6F4E37')
    draw = ImageDraw.Draw(img)
    draw.ellipse([w*0.25, h*0.25, w*0.75, h*0.75], fill='#D4A373')
    img.save(os.path.join(images_dir, f'avatar-{name}.png'))
    print(f'avatar-{name} OK')

print('\nAll images generated!')
