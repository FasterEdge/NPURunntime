# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 地平线 Horizon 征程 BPU 推理示例（hb_mapper / hbdk）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.bin"           # TODO: 替换为 .bin 模型路径（hb_mapper 量化产物）
INPUT_SIZE = (640, 640)            # TODO: 按模型输入尺寸修改

def load_model(path):
    # TODO: 使用地平线 BPU SDK（hbdk / hb_mapper）加载量化模型
    # 参考官方样例：hb_mapper 转换 + 运行时推理
    return None

def preprocess(image_path):
    import cv2
    img = cv2.imread(image_path)
    img = cv2.resize(img, INPUT_SIZE)
    img = img.astype(np.float32)
    return np.transpose(img, (2, 0, 1))[None]  # NCHW

def run_inference(model, data):
    # TODO: 调用 BPU 推理接口，返回输出
    return []

if __name__ == "__main__":
    model = load_model(MODEL_PATH)
    data = preprocess("example.png")  # TODO: 替换输入图片
    for _ in range(3):
        run_inference(model, data)
    start = time.time()
    outputs = run_inference(model, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")