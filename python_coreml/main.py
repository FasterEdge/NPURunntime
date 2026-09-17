# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# Apple Neural Engine 推理示例（Core ML / coremltools）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.mlpackage"     # TODO: 替换为 .mlpackage/.mlmodel 路径
INPUT_NAME = "image"               # TODO: 按模型输入名修改
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_model(path):
    import coremltools as ct
    model = ct.models.MLModel(path)
    return model

def run_inference(model, data):
    out = model.predict({INPUT_NAME: data})  # TODO: 按输入名/预处理修改
    return out

if __name__ == "__main__":
    model = load_model(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(model, data)
    start = time.time()
    outputs = run_inference(model, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", outputs)