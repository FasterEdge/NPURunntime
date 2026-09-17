// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// MNN NPU backend C++ 推理示例
// 动态参数均用注释占位，按实际模型修改

#include <iostream>
#include <chrono>
#include <MNN/Interpreter.hpp>
#include <MNN/ImageProcess.hpp>

int main() {
    // ===== 动态参数（按实际模型修改）=====
    const char* model_path = "model.mnn";   // TODO: 替换为 .mnn 模型路径

    std::shared_ptr<MNN::Interpreter> net(MNN::Interpreter::createFromFile(model_path));
    if (!net) { std::cerr << "load model failed" << std::endl; return -1; }

    MNN::ScheduleConfig config;
    config.type = MNN_FORWARD_NN;           // TODO: NPU backend（MNN_FORWARD_NN/OPENCL）
    auto session = net->createSession(config);

    // TODO: 获取输入 tensor（net->getSessionInput），填充输入数据

    // 预热
    for (int i = 0; i < 3; i++) {
        net->runSession(session);
    }

    auto start = std::chrono::steady_clock::now();
    net->runSession(session);
    auto end = std::chrono::steady_clock::now();
    std::cout << "inference time: "
              << std::chrono::duration<double, std::milli>(end - start).count()
              << " ms" << std::endl;

    // TODO: 读取输出 net->getSessionOutput
    return 0;
}