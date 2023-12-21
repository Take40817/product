import os
from flask import Flask, request, render_template
from model import predict
from process import recog_img
import os

PREPROCESS_FOLDER = "./static/preprocess_image"
PROCESSED_FOLDER = "./static/processed_image"

app = Flask(__name__)


@app.route("/")
def index():
    # index.htmlを開く際にprocessed_imgageを空にする
    for f in os.listdir(PROCESSED_FOLDER):
        os.remove(os.path.join(PROCESSED_FOLDER, f))
    return render_template("index.html")


@app.route("/image")
def image():
    return render_template("image.html")


@app.route("/rule")
def rule():
    return render_template("rule.html")


@app.route("/upload", methods=["GET", "POST"])
def process_use_files():
    if request.method == "POST":
        upload_file = request.files["upload_file"]
        # ファイルが選択されていない場合の処理
        if "upload_file" not in request.files or upload_file.filename == "":
            return render_template("error.html", message="ファイルを正しく選択してください")
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
        processed_file = request.form.get("processed_file")
        label, probability = predict(processed_file)
        if label == "alaba":
            return render_template(
                "alaba.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "bellingham":
            return render_template(
                "bellingham.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "camavinga":
            return render_template(
                "camavinga.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "carvajal":
            return render_template(
                "carvajal.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "ceballos":
            return render_template(
                "ceballos.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "courtois":
            return render_template(
                "courtois.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "joselu":
            return render_template(
                "joselu.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "kroos":
            return render_template(
                "kroos.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "militao":
            return render_template(
                "militao.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "modric":
            return render_template(
                "modric.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "nacho":
            return render_template(
                "nacho.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "rodrygo":
            return render_template(
                "rodrygo.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "taa":
            return render_template(
                "taa.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "valverde":
            return render_template(
                "valverde.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "vazquez":
            return render_template(
                "vazwuez.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )
        elif label == "vinicius":
            return render_template(
                "vinicius.html",
                probability=int(probability),
                label=label,
                img_path=processed_file,
            )


@app.route("/non_processed", methods=["GET", "POST"])
def non_processed_files():
    if request.method == "POST":
        # processed_image内の一つの写真を使って予測
        upload_file = request.files["upload_file"]
        # ファイルが選択されていない場合の処理
        if "upload_file" not in request.files or upload_file.filename == "":
            return render_template("error.html", message="ファイルを正しく選択してください")
        img_path = os.path.join(PROCESSED_FOLDER, upload_file.filename)
        upload_file.save(img_path)
        label, probability = predict(img_path)
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
        elif label == "camavinga":
            return render_template(
                "camavinga.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "carvajal":
            return render_template(
                "carvajal.html",
                probability=int(probability),
                label=label,
                img_path=img_path,
            )
        elif label == "ceballos":
            return render_template(
                "ceballos.html",
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
        elif label == "joselu":
            return render_template(
                "joselu.html",
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
        elif label == "vazquez":
            return render_template(
                "vazwuez.html",
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
