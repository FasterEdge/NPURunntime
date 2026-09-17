# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# MNN NPU backend 推理示例（Python 绑定）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np
import MNN

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.mnn"           # TODO: 替换为 .mnn 模型路径
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改（NCHW）

def load_interpreter(path):
    interpreter = MNN.Interpreter(path)
    config = {}
    config["backend"] = MNN.MNN_FORWARD_NN  # TODO: NPU backend（MNN_FORWARD_NN/OPENCL 等）
    session = interpreter.createSession(config)
    return interpreter, session

def run_inference(interpreter, session, data):
    input_tensor = interpreter.getSessionInput(session)
    MNN_data = MNN.Tensor(input_tensor, MNN.Tensor_DimensionType_Caffe)
    # TODO: 填充输入数据（按 backend 支持的 layout 修改）
    interpreter.resizeTensor(input_tensor, INPUT_SHAPE)
    interpreter.resizeSession(session)
    interpreter.runSession(session)
    output_tensor = interpreter.getSessionOutput(session)  # TODO: 按输出名修改
    return np.array(output_tensor.getData())

if __name__ == "__main__":
    interpreter, session = load_interpreter(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(interpreter, session, data)
    start = time.time()
    out = run_inference(interpreter, session, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", out.shape)