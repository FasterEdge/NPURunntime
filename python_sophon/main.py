# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 算能 Sophon TPU 推理示例（SAIL）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.bmodel"        # TODO: 替换为 .bmodel 路径（TPU-MLIR 转换产物）
DEVICE_ID = 0                      # TODO: TPU 设备号

def load_engine(path, device_id):
    import sophon.sail as sail
    engine = sail.Engine(path, device_id, sail.IOMode.SYSI)  # TODO: 按 IO 模式修改
    return engine

def run_inference(engine, data):
    graph_name = engine.get_graph_names()[0]      # TODO: 按模型图名修改
    input_name = engine.get_input_names(graph_name)[0]   # TODO: 按输入名修改
    output_name = engine.get_output_names(graph_name)[0] # TODO: 按输出名修改
    input_tensor = sail.Tensor(engine.get_handle(), data.shape, sail.Dtype.BM_FLOAT32)  # TODO: 按 dtype 修改
    engine.process(graph_name, {input_name: input_tensor})
    return engine.get_output(graph_name, output_name)

if __name__ == "__main__":
    engine = load_engine(MODEL_PATH, DEVICE_ID)
    data = np.zeros((1, 3, 640, 640), dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(engine, data)
    start = time.time()
    out = run_inference(engine, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", out.shape)