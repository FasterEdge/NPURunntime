# NPURunntime

多种 NPU 平台、多种语言的神经网络推理运行时示例集。

> 说明：每个子目录是一个独立的 NPU 推理运行时示例。**所有与模型强相关的动态参数（模型路径、输入/输出张量名、输入尺寸、类别数、量化参数、NPU 设备号、加速库/后端选择等）均以 `TODO` 注释占位**，请按实际模型填写后使用。示例中的 `example.png` / `example2.png` 等输入图片与模型文件需自行准备。

## 目录索引

### Python

| 目录 | NPU 平台 | 运行库/框架 | 说明 |
|------|----------|-------------|------|
| [python_ascend](python_ascend/) | 华为昇腾 Ascend | CANN (pyACL) / MindSpore Lite | 昇腾 NPU 推理（ACL 内存/流管理） |
| [python_rknn](python_rknn/) | 瑞芯微 Rockchip | rknn-toolkit2 | RK3588/RK3576 等 NPU 推理（含量化） |
| [python_cambricon](python_cambricon/) | 寒武纪 Cambricon | MagicMind / CNRT | MLU 推理（PyMagicMind） |
| [python_sophon](python_sophon/) | 算能 Sophon | sail | BM1684X 等 TPU 推理（SAIL 封装） |
| [python_horizon](python_horizon/) | 地平线 Horizon | hb_mapper / hbdk | 征程 BPU 推理（工具链转换） |
| [python_qualcomm](python_qualcomm/) | 高通 Qualcomm | QNN / qai-hub | Hexagon NPU 推理（QNN 后端） |
| [python_mediatek](python_mediatek/) | 联发科 MediaTek | NeuroPilot | APU 推理（NeuroPilot SDK） |
| [python_coreml](python_coreml/) | Apple | coremltools | Apple Neural Engine 推理（Core ML） |
| [python_openvino_npu](python_openvino_npu/) | Intel | openvino | NPU 插件推理（`device="NPU"`） |
| [python_ort_npu](python_ort_npu/) | 通用（NPU EP） | onnxruntime | ONNX Runtime NPU 执行提供程序 |
| [python_tflite_npu](python_tflite_npu/) | 通用（delegate） | tensorflow | TFLite NNAPI / Hexagon 委派推理 |
| [python_executorch](python_executorch/) | 移动端 NPU | executorch | ExecuTorch NPU backend（高通/联发科） |
| [python_ncnn](python_ncnn/) | 通用（Vulkan） | ncnn | NCNN Vulkan 加速推理 |
| [python_mnn](python_mnn/) | 通用（NPU） | MNN | MNN NPU backend 推理 |
| [python_paddlelite](python_paddlelite/) | 通用（国产 NPU） | paddlelite | Paddle Lite 华为/瑞芯微 NPU 推理 |

### C++

| 目录 | NPU 平台 | 运行库/框架 | 说明 |
|------|----------|-------------|------|
| [cpp_ascend](cpp_ascend/) | 华为昇腾 Ascend | CANN (ACL) | 昇腾 NPU C++ 推理（aclrt 运行时） |
| [cpp_rknn](cpp_rknn/) | 瑞芯微 Rockchip | RKNN API | RKNPU2 C++ 推理 |
| [cpp_qualcomm](cpp_qualcomm/) | 高通 Qualcomm | SNPE / QNN | Hexagon NPU C++ 推理 |
| [cpp_openvino_npu](cpp_openvino_npu/) | Intel | OpenVINO C++ | NPU 插件 C++ 推理 |
| [cpp_ncnn](cpp_ncnn/) | 通用（Vulkan） | ncnn C++ | NCNN Vulkan 加速推理 |
| [cpp_mnn](cpp_mnn/) | 通用（NPU） | MNN C++ | MNN NPU backend 推理 |

### Go

| 目录 | NPU 平台 | 运行库/框架 | 说明 |
|------|----------|-------------|------|
| [go_onnxruntime](go_onnxruntime/) | 通用（NPU EP） | onnxruntime_go | Go 版 ONNX Runtime（NPU 执行提供程序） |
| [go_tflite](go_tflite/) | 通用（delegate） | go-tflite (+NNAPI) | Go 版 TFLite NNAPI 委派推理 |

### Rust

| 目录 | NPU 平台 | 运行库/框架 | 说明 |
|------|----------|-------------|------|
| [rust_ort](rust_ort/) | 通用（NPU EP） | ort | ONNX Runtime Rust 绑定（NPU 执行提供程序） |

### Java

| 目录 | NPU 平台 | 运行库/框架 | 说明 |
|------|----------|-------------|------|
| [java_onnxruntime](java_onnxruntime/) | 通用（NPU EP） | onnxruntime-java | Java 版 ONNX Runtime（NPU 执行提供程序） |
| [java_djl](java_djl/) | 多平台（NPU backend） | Deep Java Library | DJL 统一加载 + NPU 后端 |

### C# (.NET)

| 目录 | NPU 平台 | 运行库/框架 | 说明 |
|------|----------|-------------|------|
| [csharp_onnxruntime](csharp_onnxruntime/) | 通用（NPU EP） | Microsoft.ML.OnnxRuntime | .NET 版 ONNX Runtime（NPU 执行提供程序） |

### JavaScript / Node.js

| 目录 | NPU 平台 | 运行库/框架 | 说明 |
|------|----------|-------------|------|
| [node_onnxruntime](node_onnxruntime/) | 通用（NPU EP） | onnxruntime-node | Node.js 版 ONNX Runtime（NPU 执行提供程序） |
| [node_webnn](node_webnn/) | 通用（WebNN） | WebNN API | WebNN NPU 后端推理 |

## 使用方式

1. 进入对应子目录，查看该语言/平台的 `main` 文件与依赖清单。
2. 将 `TODO` 占位处替换为实际模型路径、输入输出名、输入尺寸、类别数、量化参数与 NPU 设备号等动态参数。
3. 准备输入图片与模型文件（部分平台需先经官方工具链转换为 NPU 专用格式），按各目录的构建/运行说明执行（Python `requirements.txt`、C++ `CMakeLists.txt`、Go `go.mod`、Rust `Cargo.toml`、Java `pom.xml`、C# `.csproj`、Node `package.json`）。
