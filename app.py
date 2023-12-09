import os
from flask import Flask, request, render_template
from model import predict

UPLOAD_FOLDER = "./static/result_image"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload_user_files():
    if request.method == "POST":
        upload_file = request.files["upload_file"]
        img_path = os.path.join(UPLOAD_FOLDER, upload_file.filename)
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
