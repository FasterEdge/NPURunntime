# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 高通 Qualcomm Hexagon NPU 推理示例（QNN / qai-hub）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.onnx"          # TODO: 替换为模型路径（onnx/tflite）
DEVICE = "Snapdragon 8 Elite QNN"  # TODO: 目标设备（qai-hub 设备名）
INPUT_NAME = "images"              # TODO: 按模型输入名修改
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_model(path):
    import qai_hub as hub
    model = hub.upload_model(path)
    compile_job = hub.submit_compile_job(
        model, device=hub.Device(DEVICE),
        input_specs={INPUT_NAME: INPUT_SHAPE},
    )
    return compile_job.get_target_model()

def run_inference(target_model, data):
    import qai_hub as hub
    inference_job = hub.submit_inference_job(
        model=target_model,
        inputs={INPUT_NAME: [data]},
    )
    return inference_job.download_output_data()

if __name__ == "__main__":
    target_model = load_model(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(target_model, data)
    start = time.time()
    outputs = run_inference(target_model, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")