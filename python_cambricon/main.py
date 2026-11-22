# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 寒武纪 Cambricon MLU 推理示例（PyMagicMind）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.mm"            # TODO: 替换为 MagicMind 编译产物路径
DEVICE_ID = 0                      # TODO: MLU 设备号

def load_model(path, device_id):
    import magicmind               # PyMagicMind：随 Neuware SDK 提供
    model = magicmind.Model()
    model.deserialize_from_file(path)  # TODO: 或从 ONNX 构建网络
    engine = model.create_i_engine()
    context = engine.create_i_context()
    return context

def run_inference(context, data):
    # TODO: 构造输入/输出 tensor -> context.enqueue -> 同步后取输出
    # 未实现前必须抛错，避免"done 0 outputs"的假成功路径（本机无 MLU 与 Neuware SDK）。
    raise NotImplementedError(
        "本示例的推理主体尚未实现：本机没有对应 NPU 硬件与厂商 SDK。\n"
        "  请按 TODO 注释补齐 context.enqueue 的真实调用后删除本行；\n"
        "  在此之前直接运行会抛错而不是打印假的 'done 0 outputs'。"
    )

if __name__ == "__main__":
    context = load_model(MODEL_PATH, DEVICE_ID)
    data = np.zeros((1, 3, 640, 640), dtype=np.float32)  # TODO: 预处理（NCHW）
    for _ in range(3):
        run_inference(context, data)
    start = time.time()
    outputs = run_inference(context, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")