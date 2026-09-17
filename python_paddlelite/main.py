# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# Paddle Lite 国产 NPU 推理示例（华为昇腾/瑞芯微）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np
from paddlelite.lite import *  # TODO: 需安装 paddlelite（官方发布包）

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.nb"            # TODO: 替换为 .nb 模型路径（Paddle Lite 优化产物）
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_predictor(path):
    # TODO: 选择 NPU 后端：华为昇腾(NPU)/瑞芯微(RKNPU) 用 MobileConfig + set_valid_places
    config = MobileConfig()
    config.set_model_from_file(path)
    config.set_power_mode(PowerMode.LITE_POWER_HIGH)  # TODO: 功耗模式
    return create_paddle_predictor(config)

def run_inference(predictor, data):
    input_tensor = predictor.get_input(0)  # TODO: 按输入索引修改
    input_tensor.from_numpy(data)
    predictor.run()
    out = predictor.get_output(0)  # TODO: 按输出索引修改
    return out.numpy()

if __name__ == "__main__":
    predictor = load_predictor(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(predictor, data)
    start = time.time()
    out = run_inference(predictor, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", out.shape)