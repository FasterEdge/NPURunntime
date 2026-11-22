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

## 可验证性矩阵（machine-readable）

仓库根的 `matrix.json` 记录每个示例的真实可验证性状态，由脚本从源码提取生成，**不是手写**：

```
python tools/gen_matrix.py          # 重新提取并覆盖 matrix.json
python tools/gen_matrix.py --check  # 校验 matrix.json 与源码一致，不一致退出码 1
```

`--check` 只校验**与工具链无关的源码事实**（未消除的 TODO、推理调用是否存在、模型格式、
入口文件、缺失依赖清单），因此可以在 CI 里稳定运行。它有意不校验 `status` / `compile_check` /
`evidence` 字段——这三个字段依赖本机是否装了 g++ / node / gofmt / dotnet / cargo 与 ONNX Runtime
共享库，跨机器比对会产生假失败。想确认状态字段是否最新，跑一次
`python tools/gen_matrix.py && PYTHON_BIN=<你的 venv python> python tools/verify_matrix.py`。

状态定义（三选一，判定规则见 `tools/gen_matrix.py` 顶部 docstring）：

| 状态 | 含义 |
|------|------|
| `verified` | 由 `tools/verify_matrix.py` 真实构建并运行通过，命令与输出记录在 `matrix.json` 的 `evidence` 字段 |
| `compilable` | 语法/编译检查通过（Python `py_compile` 等价语法检查、Go `gofmt -l`、JS `node --check`、C++ `g++ -fsyntax-only`），但推理调用尚未执行（缺模型或运行库） |
| `placeholder` | 存在未消除 `TODO`，或推理调用缺失/被注释掉，或语法编译检查失败 |

> **关于"不要假装能跑真实 NPU"**：本仓库所有 Python 示例都能通过语法检查，但**没有一条推理路径在本机真正执行过**，
> 因为本机没有昇腾/瑞芯微/高通/地平线/寒武纪 NPU，也没有 CANN / RKNPU2 / SNPE / QNN / NeuroPilot / Core ML 等厂商 SDK。
> 每个示例缺失的具体依赖见 `matrix.json` 的 `missing_deps` 字段。
> 因此除 `go_onnxruntime`（ONNX Runtime CPU EP 实跑验证，模型借用 ModelRunntime 的 `yolov5n.onnx`）外，其余示例一律标为 `placeholder`——
> 这不是"未完成"，而是对硬件边界的诚实标注：**没有硬件与 SDK，就不宣称跑通**。
> 用户提供的 `run_inference` 里 `return []` / `return None` 的示例（python_ascend / python_cambricon /
> python_executorch / python_horizon / python_mediatek）在 `matrix.json` 的
> `signals.shell_functions` 字段里被逐一点名。

## 使用方式

1. 进入对应子目录，查看该语言/平台的 `main` 文件与依赖清单。
2. 将 `TODO` 占位处替换为实际模型路径、输入输出名、输入尺寸、类别数、量化参数与 NPU 设备号等动态参数。
3. 准备输入图片与模型文件（部分平台需先经官方工具链转换为 NPU 专用格式），按各目录的构建/运行说明执行（Python `requirements.txt`、C++ `CMakeLists.txt`、Go `go.mod`、Rust `Cargo.toml`、Java `pom.xml`、C# `.csproj`、Node `package.json`）。

> Go 示例依赖本机 C 运行时：`go_onnxruntime` 需要 ONNX Runtime C 共享库（可用 `ort.SetSharedLibraryPath` 指定路径）；`go_tflite` 需要 TensorFlow Lite C API 头文件与 `libtensorflowlite_c.so`，并按上游 go-tflite 文档设置 `CGO_CFLAGS` / `CGO_LDFLAGS`。模型与这些原生依赖未包含在本仓库内。
