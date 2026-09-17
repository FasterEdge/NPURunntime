# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 瑞芯微 Rockchip NPU 推理示例（rknn-toolkit2）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.rknn"          # TODO: 替换为 .rknn 模型路径（RKNN 转换产物）
TARGET = "rk3588"                  # TODO: 目标平台 rk3588/rk3576/rk3566...
DEVICE_ID = None                   # TODO: 设备串口/地址（None=模拟器）

def load_rknn(path):
    from rknn.api import RKNN
    rknn = RKNN(verbose=False)
    ret = rknn.load_rknn(path)
    if ret != 0:
        raise RuntimeError(f"load_rknn failed: {ret}")
    ret = rknn.init_runtime(target=TARGET, device_id=DEVICE_ID)
    if ret != 0:
        raise RuntimeError(f"init_runtime failed: {ret}")
    return rknn

def run_inference(rknn, data):
    return rknn.inference(inputs=[data])  # TODO: 多输入时传入列表

if __name__ == "__main__":
    rknn = load_rknn(MODEL_PATH)
    data = np.zeros((1, 640, 640, 3), dtype=np.uint8)  # TODO: 预处理（NHWC）
    for _ in range(3):
        run_inference(rknn, data)
    start = time.time()
    outputs = run_inference(rknn, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")
    rknn.release()