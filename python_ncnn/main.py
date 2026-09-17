# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# NCNN Vulkan 加速推理示例（Python 绑定）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np
import ncnn

# ===== 动态参数（按实际模型修改）=====
PARAM_PATH = "model.param"         # TODO: 替换为 .param 路径
BIN_PATH = "model.bin"             # TODO: 替换为 .bin 路径
INPUT_NAME = "input"               # TODO: 按模型输入名修改
OUTPUT_NAME = "output"             # TODO: 按模型输出名修改
INPUT_SIZE = (640, 640)            # TODO: 按模型输入尺寸修改
USE_VULKAN = True                  # TODO: Vulkan 加速开关（需 GPU）

def load_net(param, bin_path):
    net = ncnn.Net()
    net.opt.use_vulkan_compute = USE_VULKAN  # TODO: Vulkan NPU 加速
    net.load_param(param)
    net.load_model(bin_path)
    return net

def run_inference(net, data):
    ex = net.create_extractor()
    ex.input(INPUT_NAME, data)
    ret, out = ex.extract(OUTPUT_NAME)  # TODO: 按输出名修改
    if ret != 0:
        raise RuntimeError(f"extract failed: {ret}")
    return out

if __name__ == "__main__":
    net = load_net(PARAM_PATH, BIN_PATH)
    data = ncnn.Mat.from_pixels(np.zeros((*INPUT_SIZE, 3), dtype=np.uint8), ncnn.Mat.PixelType.PIXEL_BGR, INPUT_SIZE[0], INPUT_SIZE[1])  # TODO: 预处理
    for _ in range(3):
        run_inference(net, data)
    start = time.time()
    out = run_inference(net, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", out.w, out.h, out.c)