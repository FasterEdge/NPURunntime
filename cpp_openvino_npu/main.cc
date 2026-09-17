// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// Intel OpenVINO NPU 插件 C++ 推理示例
// 动态参数均用注释占位，按实际模型修改

#include <iostream>
#include <chrono>
#include <openvino/openvino.hpp>

int main() {
    // ===== 动态参数（按实际模型修改）=====
    const std::string model_path = "model.xml";   // TODO: 替换为 OpenVINO IR 模型路径
    const std::string device = "NPU";             // TODO: 目标设备 NPU/GPU/CPU

    ov::Core core;
    auto model = core.read_model(model_path);
    auto compiled = core.compile_model(model, device);  // TODO: NPU 需安装驱动/插件
    auto infer_request = compiled.create_infer_request();

    // TODO: 填充输入数据（读图、预处理 -> NCHW）
    // float* input = infer_request.get_input_tensor().data<float>();

    // 预热
    for (int i = 0; i < 3; i++) {
        infer_request.infer();
    }

    auto start = std::chrono::steady_clock::now();
    infer_request.infer();
    auto end = std::chrono::steady_clock::now();
    std::cout << "inference time: "
              << std::chrono::duration<double, std::milli>(end - start).count()
              << " ms" << std::endl;

    // TODO: 读取输出 infer_request.get_output_tensor()
    return 0;
}