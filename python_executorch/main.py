# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# ExecuTorch 移动端 NPU 推理示例（高通/联发科 backend）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.pte"           # TODO: 替换为 .pte 模型路径（ExecuTorch 导出产物）
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_module(path):
    # TODO: 使用 ExecuTorch 运行时加载 .pte 模块，选择 NPU backend
    # 高通/联发科 backend 参考官方样例（executorch 导出 + 运行时）
    import executorch  # noqa: F401
    return None

def run_inference(module, data):
    # TODO: 调用 module.forward(data) 并读取输出
    return []

if __name__ == "__main__":
    module = load_module(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(module, data)
    start = time.time()
    outputs = run_inference(module, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")