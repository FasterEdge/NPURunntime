// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// 瑞芯微 Rockchip NPU C++ 推理示例（RKNPU2 API）
// 动态参数均用注释占位，按实际模型修改

#include <iostream>
#include <chrono>
#include "rknn_api.h"   // TODO: RKNPU2 头文件（随 rknn-toolkit2 提供）

int main() {
    // ===== 动态参数（按实际模型修改）=====
    const char* model_path = "model.rknn";   // TODO: 替换为 .rknn 模型路径

    rknn_context ctx = 0;
    int ret = rknn_init(&ctx, const_cast<char*>(model_path), 0, 0, nullptr);
    if (ret != RKNN_SUCC) { std::cerr << "rknn_init failed: " << ret << std::endl; return -1; }

    // TODO: rknn_query 获取输入/输出属性，分配缓冲，填充输入数据

    // 预热
    for (int i = 0; i < 3; i++) {
        // rknn_run(ctx, nullptr);  // TODO: 或 rknn_inputs_set + rknn_run
    }

    auto start = std::chrono::steady_clock::now();
    // rknn_run(ctx, nullptr);      // TODO
    auto end = std::chrono::steady_clock::now();
    std::cout << "inference time: "
              << std::chrono::duration<double, std::milli>(end - start).count()
              << " ms" << std::endl;

    // TODO: 读取输出，rknn_destroy
    return 0;
}