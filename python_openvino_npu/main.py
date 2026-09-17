# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# Intel OpenVINO NPU 插件推理示例
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np
import openvino as ov

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.xml"           # TODO: 替换为 OpenVINO IR 模型路径（.xml）
DEVICE = "NPU"                     # TODO: 目标设备 NPU/GPU/CPU
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_model(path):
    core = ov.Core()
    model = core.read_model(path)
    return core.compile_model(model, DEVICE)  # TODO: NPU 需安装驱动/插件

def run_inference(compiled, data):
    infer_request = compiled.create_infer_request()
    infer_request.set_input_tensor(ov.Tensor(np.ascontiguousarray(data)))
    infer_request.infer()
    return infer_request.get_output_tensor().data  # TODO: 按输出名修改

if __name__ == "__main__":
    compiled = load_model(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(compiled, data)
    start = time.time()
    out = run_inference(compiled, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", out.shape)