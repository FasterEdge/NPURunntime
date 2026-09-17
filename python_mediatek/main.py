# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 联发科 MediaTek APU 推理示例（NeuroPilot SDK）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.neuron"        # TODO: 替换为 NeuroPilot 转换产物（.neuron/.dla）
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_model(path):
    # TODO: 使用 NeuroPilot SDK（Neuron SDK）加载 DLA 模型
    # 参考官方样例：模型转换 + APU 运行时推理
    return None

def run_inference(model, data):
    # TODO: 调用 APU 推理接口，返回输出
    return []

if __name__ == "__main__":
    model = load_model(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(model, data)
    start = time.time()
    outputs = run_inference(model, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")