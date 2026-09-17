# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# TensorFlow Lite NPU 委派推理示例（NNAPI / Hexagon）
# 动态参数均用注释占位，按实际模型修改

import time
import numpy as np
import tensorflow as tf

# ===== 动态参数（按实际模型修改）=====
MODEL_PATH = "model.tflite"        # TODO: 替换为 .tflite 模型路径
INPUT_SHAPE = (1, 640, 640, 3)     # TODO: 按模型输入 shape 修改（NHWC）

def load_interpreter(path):
    # TODO: 选择 NNAPI（Android）或 Hexagon 委托（需 libhexagon_delegate.so）
    delegate = tf.lite.experimental.load_delegate("libhexagon_delegate.so")  # TODO: Hexagon 委托路径
    interpreter = tf.lite.Interpreter(model_path=path, experimental_delegates=[delegate])
    interpreter.allocate_tensors()
    return interpreter

def run_inference(interpreter, data):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.set_tensor(input_details[0]["index"], data)
    interpreter.invoke()
    return [interpreter.get_tensor(d["index"]) for d in output_details]

if __name__ == "__main__":
    interpreter = load_interpreter(MODEL_PATH)
    data = np.zeros(INPUT_SHAPE, dtype=np.float32)  # TODO: 预处理
    for _ in range(3):
        run_inference(interpreter, data)
    start = time.time()
    outputs = run_inference(interpreter, data)
    print(f"inference time: {time.time()-start:.4f}s")
    print("done", len(outputs), "outputs")