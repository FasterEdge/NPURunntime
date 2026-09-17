// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// 华为昇腾 Ascend NPU C++ 推理示例（CANN ACL）
// 动态参数均用注释占位，按实际模型修改

#include <iostream>
#include <chrono>
#include "acl/acl.h"   // TODO: CANN 头文件（随 Ascend-cann-toolkit 提供）

int main() {
    // ===== 动态参数（按实际模型修改）=====
    const char* model_path = "model.om";   // TODO: 替换为 .om 离线模型路径（atc 转换产物）
    int32_t device_id = 0;                 // TODO: NPU 设备号

    aclError ret = aclInit(nullptr);
    if (ret != ACL_SUCCESS) { std::cerr << "aclInit failed: " << ret << std::endl; return -1; }
    ret = aclrtSetDevice(device_id);
    if (ret != ACL_SUCCESS) { std::cerr << "setDevice failed: " << ret << std::endl; return -1; }

    uint32_t model_id = 0;
    ret = aclmdlLoadFromFile(model_path, &model_id);
    if (ret != ACL_SUCCESS) { std::cerr << "load model failed: " << ret << std::endl; return -1; }

    // TODO: 创建输入/输出 dataset（aclmdlCreateDataset / aclCreateDataBuf）
    // TODO: 填充输入数据（aclrtMemcpy 到设备侧）

    // 预热
    for (int i = 0; i < 3; i++) {
        // aclmdlExecute(model_id, input_dataset, output_dataset);  // TODO
    }

    auto start = std::chrono::steady_clock::now();
    // aclmdlExecute(model_id, input_dataset, output_dataset);      // TODO
    auto end = std::chrono::steady_clock::now();
    std::cout << "inference time: "
              << std::chrono::duration<double, std::milli>(end - start).count()
              << " ms" << std::endl;

    // TODO: 销毁 dataset/buf，aclmdlUnload，aclrtResetDevice，aclFinalize
    return 0;
}