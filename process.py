import face_recognition
from PIL import Image, ImageDraw
import os


def recog_img(input_filename, out_jpg):
    # 画像を読み込む
    load_image = face_recognition.load_image_file(input_filename)

    # 認識させたい画像から顔検出する
    face_locations = face_recognition.face_locations(load_image, model="hog")

    pil_image = Image.fromarray(load_image)
    draw = ImageDraw.Draw(pil_image)

    # 検出した顔分ループする
    for i, (top, right, bottom, left) in enumerate(face_locations):
        # 顔の領域を切り抜く
        face_image = pil_image.crop((left, top, right, bottom))

        # 切り抜いた顔の保存
        save_path = os.path.join(out_jpg, f"face_{i}.jpg")
        face_image.save(save_path)

    del draw
