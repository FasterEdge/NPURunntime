# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# ONNX Runtime NPU 执行提供程序（EP）推理示例
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np
import onnxruntime as ort

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.onnx"          # TODO: 替换为 .onnx 模型路径
PROVIDER = "QNNExecutionProvider"  # TODO: QNN/OpenVINO/CoreML/VitisAI 等 NPU EP
INPUT_NAME = "images"              # TODO: 按模型输入名修改
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_session(path):
    opts = ort.SessionOptions()
    # NPU EP 缺失时回退 CPU
    return ort.InferenceSession(path, opts, providers=[PROVIDER, "CPUExecutionProvider"])

def run_inference(session, data):
    return session.run(None, {INPUT_NAME: data})

if __name__ == "__main__":
    session = load_session(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(session, data)
    start = time.time()
    outputs = run_inference(session, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")