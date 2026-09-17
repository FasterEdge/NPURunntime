// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// 高通 Qualcomm Hexagon NPU C++ 推理示例（SNPE / QNN）
// 动态参数均用注释占位，按实际模型修改

#include <iostream>
#include <chrono>
// #include "SNPE/SNPE.hpp"          // TODO: SNPE 头文件
// #include "QnnModel.hpp"           // TODO: QNN 头文件

int main() {
    // ===== 动态参数（按实际模型修改）=====
    const char* model_path = "model.dlc";   // TODO: 替换为 .dlc(SNPE)/.bin(QNN) 模型路径

    // TODO: 构建 SNPE/QNN Runtime，加载模型到 Hexagon NPU
    // SNPE: snpe::SNPEFactory::getSNPE() -> load() -> execute()
    // QNN:  QnnModel 加载 + 创建 backend/graph

    // 预热
    for (int i = 0; i < 3; i++) {
        // TODO: 推理
    }

    auto start = std::chrono::steady_clock::now();
    // TODO: 推理
    auto end = std::chrono::steady_clock::now();
    std::cout << "inference time: "
              << std::chrono::duration<double, std::milli>(end - start).count()
              << " ms" << std::endl;

    return 0;
}