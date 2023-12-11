import os
from flask import Flask, request, render_template
from model import predict
from process import recog_img
import os

PREPROCESS_FOLDER = "./static/preprocess_image"
PROCESSED_FOLDER = "./static/processed_image"
UPLOAD_FOLDER = "./static/result_image"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def process_use_files():
    if request.method == "POST":
        upload_file = request.files["upload_file"]
        img_path = os.path.join(PREPROCESS_FOLDER, upload_file.filename)
        upload_file.save(img_path)
        recog_img(img_path, PROCESSED_FOLDER)
        processed_image_paths = [
            os.path.join(PROCESSED_FOLDER, filename)
            for filename in os.listdir(PROCESSED_FOLDER)
            if filename.endswith((".jpg", ".jpeg", ".png", ".gif"))
        ]
        print(processed_image_paths)
        # PREPROCESS_FOLDER内の画像を削除
        os.remove(img_path)
        return render_template(
            "process.html", processed_image_paths=processed_image_paths
        )


@app.route("/processed", methods=["GET", "POST"])
def upload_user_files():
    if request.method == "POST":
        # processed_image内の一つの写真を使って予測
        processed_file = request.files["processed_file"]
        img_path = os.path.join(UPLOAD_FOLDER, processed_file.filename)
        processed_file.save(img_path)
        label, probability = predict(img_path)
        # ここらへんでprocessed_imageの中身を消すべし
        if label == "alaba":
            return render_template(
                "alaba.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "bellingham":
            return render_template(
                "bellingham.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        if label == "carvajal":
            return render_template(
                "carvajal.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "courtois":
            return render_template(
                "courtois.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "kroos":
            return render_template(
                "kroos.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "militao":
            return render_template(
                "militao.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "modric":
            return render_template(
                "modric.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "nacho":
            return render_template(
                "nacho.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "rodrygo":
            return render_template(
                "rodrygo.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "taa":
            return render_template(
                "taa.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "valverde":
            return render_template(
                "valverde.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "vinicius":
            return render_template(
                "vinicius.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )


if __name__ == "__main__":
    app.run(debug=True)
