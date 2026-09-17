# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 华为昇腾 Ascend NPU 推理示例（CANN pyACL）
# 动态参数均用注释占位，按实际模型修改
# 需先安装 CANN 工具链（Ascend-cann-toolkit）并配置环境变量

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.om"            # TODO: 替换为 .om 离线模型路径（atc 转换产物）
DEVICE_ID = 0                      # TODO: NPU 设备号
INPUT_SHAPE = (1, 3, 640, 640)     # TODO: 按模型输入 shape 修改

def load_model(model_path, device_id):
    import acl                    # pyACL：随 CANN 提供，无公共 pip 包
    ret = acl.init()
    assert ret == 0, f"acl.init failed: {ret}"
    ret = acl.rt.set_device(device_id)
    assert ret == 0, f"set_device failed: {ret}"
    model_id, ret = acl.mdl.load_from_file(model_path)
    assert ret == 0, f"load model failed: {ret}"
    desc = acl.mdl.create_desc()
    acl.mdl.get_desc(desc, model_id)
    return model_id, desc

def run_inference(model_id, data):
    # TODO: 构造输入 dataset -> acl.mdl.execute -> 同步后读取输出
    # 完整流程参考 CANN 官方样例（ACLNN / GE 模式）
    return []

if __name__ == "__main__":
    model_id, desc = load_model(MODEL_PATH, DEVICE_ID)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理输入
    for _ in range(3):
        run_inference(model_id, data)
    start = time.time()
    outputs = run_inference(model_id, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")
    # TODO: 释放 acl.mdl.unload / acl.rt.reset_device / acl.finalize