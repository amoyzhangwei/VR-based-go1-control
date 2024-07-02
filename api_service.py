from flask import Flask, request, jsonify
from PIL import Image, ImageDraw
import io

app = Flask(__name__)

@app.route('/mark_desk_bottom', methods=['POST'])
def mark_desk_bottom_api():
    # 从请求中获取图像
    image_file = request.files['image']
    image = Image.open(image_file.stream)

    # 创建绘图上下文
    draw = ImageDraw.Draw(image)

    # 定义矩形的坐标（这些坐标是基于示例图像的）
    xmin, ymin, xmax, ymax = 130, 300, 460, 450

    # 画矩形
    draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=5)

    # 将标注后的图像保存到字节流
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # 返回标注的坐标和图像
    response = {
        "coordinates": {
            "xmin": xmin,
            "ymin": ymin,
            "xmax": xmax,
            "ymax": ymax
        },
        "marked_image": img_byte_arr.hex()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

