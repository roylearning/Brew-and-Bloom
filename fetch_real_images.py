import os
import urllib.request

images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
os.makedirs(images_dir, exist_ok=True)

image_urls = {
    'hero-coffee.png': 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=900&auto=format&fit=crop&q=80',
    'espresso.png': 'https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=600&auto=format&fit=crop&q=80',
    'caramel-latte.png': 'https://images.unsplash.com/photo-1534778101976-62847782c213?w=600&auto=format&fit=crop&q=80',
    'cold-brew.png': 'https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?w=600&auto=format&fit=crop&q=80',
    'affogato.png': 'https://images.unsplash.com/photo-1592663527359-cf6642f54cff?w=600&auto=format&fit=crop&q=80',
    'capuccino.png': 'https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=600&auto=format&fit=crop&q=80',
    'mocha.png': 'https://images.unsplash.com/photo-1578314675249-a6910f80cc4e?w=600&auto=format&fit=crop&q=80',
    'earl-grey.png': 'https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=600&auto=format&fit=crop&q=80',
    'matcha-latte.png': 'https://images.unsplash.com/photo-1536256263959-770b48d82b0a?w=600&auto=format&fit=crop&q=80',
    'croissant.png': 'https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=600&auto=format&fit=crop&q=80',
    'blueberry-muffin.png': 'https://images.unsplash.com/photo-1607958996333-41aef7caefaa?w=600&auto=format&fit=crop&q=80',
    'cinnamon-roll.png': 'https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600&auto=format&fit=crop&q=80',
    'avatar-sarah.png': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=crop&q=80',
    'avatar-james.png': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=crop&q=80',
    'avatar-amara.png': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=crop&q=80'
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for filename, url in image_urls.items():
    filepath = os.path.join(images_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded: {filename} ({os.path.getsize(filepath):,} bytes)")
    except Exception as e:
        print(f"Failed {filename}: {e}")

print("Image fetch complete!")
