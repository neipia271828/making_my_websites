from PIL import Image
import os

def resize_image(input_path, output_dir, target_height):
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 画像を開く
    with Image.open(input_path) as img:
        # 元の幅と高さを取得
        original_width, original_height = img.size
        
        # 縦横比を維持しながら新しい幅を計算
        aspect_ratio = original_width / original_height
        new_width = int(target_height * aspect_ratio)
        
        # 画像をリサイズ
        resized_img = img.resize((new_width, target_height), Image.LANCZOS)
        
        # 元の画像の名前を取得
        base_name = os.path.basename(input_path)
        name, ext = os.path.splitext(base_name)
        
        # 出力画像のパスを作成
        output_path = os.path.join(output_dir, f"resized_{name}.png")
        
        # 画像をPNG形式で保存
        resized_img.save(output_path, format='PNG')
        
        return output_path

def resize_images_in_directory(input_dir, output_dir, target_height):
    # 入力ディレクトリ内のすべてのファイルを処理
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        # 画像ファイルのみを処理
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            output_path = resize_image(input_path, output_dir, target_height)
            print(f"画像がリサイズされ、{output_path} に保存されました。")

# 入力ディレクトリのパス
input_directory = '/Users/suzukiakiramuki/making_my_websites/my-website/images'

# 出力ディレクトリのパス
output_directory = '/Users/suzukiakiramuki/making_my_websites/my-website/resized_images'

# 目標の高さ
target_height = 500

# ディレクトリ内のすべての画像をリサイズして保存
resize_images_in_directory(input_directory, output_directory, target_height)