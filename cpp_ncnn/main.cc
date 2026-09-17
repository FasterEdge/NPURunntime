// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// NCNN Vulkan 加速 C++ 推理示例
// 动态参数均用注释占位，按实际模型修改

#include <iostream>
#include <chrono>
#include "net.h"

int main() {
    // ===== 动态参数（按实际模型修改）=====
    const char* param_path = "model.param";   // TODO: 替换为 .param 路径
    const char* bin_path = "model.bin";       // TODO: 替换为 .bin 路径

    ncnn::Net net;
    net.opt.use_vulkan_compute = true;        // TODO: Vulkan 加速开关
    if (net.load_param(param_path) != 0 || net.load_model(bin_path) != 0) {
        std::cerr << "load model failed" << std::endl;
        return -1;
    }

    ncnn::Extractor ex = net.create_extractor();
    // TODO: 填充输入（ex.input("input", mat)），设置输入名
    // ncnn::Mat in = ncnn::Mat::from_pixels(...);

    // 预热
    for (int i = 0; i < 3; i++) {
        // ex.extract("output", out);  // TODO
    }

    auto start = std::chrono::steady_clock::now();
    // ex.extract("output", out);      // TODO
    auto end = std::chrono::steady_clock::now();
    std::cout << "inference time: "
              << std::chrono::duration<double, std::milli>(end - start).count()
              << " ms" << std::endl;

    return 0;
}