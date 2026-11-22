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
    # 未实现前必须抛错，避免打印假的 'done 0 outputs'（本机无 APU 与 NeuroPilot SDK）。
    raise NotImplementedError(
        "本示例的推理主体尚未实现：本机没有对应 NPU 硬件与厂商 SDK。\n"
        "  请按 TODO 注释补齐 NeuroPilot 加载 DLA 模型 / APU 推理接口 的真实调用后删除本行；\n"
        "  在此之前直接运行会抛错而不是打印假的 'done 0 outputs'。"
    )

def run_inference(model, data):
    # TODO: 调用 APU 推理接口，返回输出
    raise NotImplementedError(
        "本示例的推理主体尚未实现：本机没有对应 NPU 硬件与厂商 SDK。\n"
        "  请按 TODO 注释补齐 NeuroPilot 加载 DLA 模型 / APU 推理接口 的真实调用后删除本行；\n"
        "  在此之前直接运行会抛错而不是打印假的 'done 0 outputs'。"
    )

if __name__ == "__main__":
    model = load_model(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(model, data)
    start = time.time()
    outputs = run_inference(model, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")