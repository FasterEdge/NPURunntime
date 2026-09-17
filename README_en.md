<div align="center">
  <img src="https://avatars.githubusercontent.com/u/245985800?s=200&v=4" alt="logo" width="100" />
  <h2>NPURunntime</h2>
  <h3>Neural Processing Unit (NPU) Inference Runtime Examples Across Platforms and Languages</h3>
</div>

### 1. Introduction

- NPURunntime is a collection of NPU inference runtime examples covering multiple NPU platforms and programming languages.
- **Each subdirectory is an independent NPU runtime example.** All model-specific dynamic parameters—including model paths, input and output tensor names, input dimensions, class counts, quantization parameters, NPU device ids, and accelerator library or backend selections—are represented by `TODO` comments and must be filled in for the actual model before use.
- Input images such as `example.png` and `example2.png`, together with the required model files, must be prepared by the user. Some platforms require converting the model to an NPU-specific format with the official toolchain first.

### 2. Python Examples

| Directory | NPU platform | Runtime / framework | Description |
|-----------|--------------|---------------------|-------------|
| [python_ascend](python_ascend/) | Huawei Ascend | CANN (pyACL) / MindSpore Lite | Ascend NPU inference with ACL memory/stream management |
| [python_rknn](python_rknn/) | Rockchip | rknn-toolkit2 | RK3588/RK3576 NPU inference with quantization |
| [python_cambricon](python_cambricon/) | Cambricon | MagicMind / CNRT | MLU inference through PyMagicMind |
| [python_sophon](python_sophon/) | Sophon | sail | BM1684X TPU inference through the SAIL wrapper |
| [python_horizon](python_horizon/) | Horizon | hb_mapper / hbdk | Journey BPU inference with toolchain conversion |
| [python_qualcomm](python_qualcomm/) | Qualcomm | QNN / qai-hub | Hexagon NPU inference with the QNN backend |
| [python_mediatek](python_mediatek/) | MediaTek | NeuroPilot | APU inference with the NeuroPilot SDK |
| [python_coreml](python_coreml/) | Apple | coremltools | Apple Neural Engine inference through Core ML |
| [python_openvino_npu](python_openvino_npu/) | Intel | openvino | NPU plugin inference with `device="NPU"` |
| [python_ort_npu](python_ort_npu/) | Generic (NPU EP) | onnxruntime | ONNX Runtime NPU execution provider |
| [python_tflite_npu](python_tflite_npu/) | Generic (delegate) | tensorflow | TFLite NNAPI / Hexagon delegate inference |
| [python_executorch](python_executorch/) | Mobile NPU | executorch | ExecuTorch NPU backend (Qualcomm / MediaTek) |
| [python_ncnn](python_ncnn/) | Generic (Vulkan) | ncnn | NCNN Vulkan-accelerated inference |
| [python_mnn](python_mnn/) | Generic (NPU) | MNN | MNN NPU backend inference |
| [python_paddlelite](python_paddlelite/) | Generic (CN NPU) | paddlelite | Paddle Lite Huawei / Rockchip NPU inference |

### 3. C++ Examples

| Directory | NPU platform | Runtime / framework | Description |
|-----------|--------------|---------------------|-------------|
| [cpp_ascend](cpp_ascend/) | Huawei Ascend | CANN (ACL) | Ascend NPU C++ inference with the aclrt runtime |
| [cpp_rknn](cpp_rknn/) | Rockchip | RKNN API | RKNPU2 C++ inference |
| [cpp_qualcomm](cpp_qualcomm/) | Qualcomm | SNPE / QNN | Hexagon NPU C++ inference |
| [cpp_openvino_npu](cpp_openvino_npu/) | Intel | OpenVINO C++ | NPU plugin C++ inference |
| [cpp_ncnn](cpp_ncnn/) | Generic (Vulkan) | ncnn C++ | NCNN Vulkan-accelerated inference |
| [cpp_mnn](cpp_mnn/) | Generic (NPU) | MNN C++ | MNN NPU backend inference |

### 4. Go Examples

| Directory | NPU platform | Runtime / framework | Description |
|-----------|--------------|---------------------|-------------|
| [go_onnxruntime](go_onnxruntime/) | Generic (NPU EP) | onnxruntime_go | ONNX Runtime in Go with the NPU execution provider |
| [go_tflite](go_tflite/) | Generic (delegate) | go-tflite (+NNAPI) | TFLite NNAPI delegate inference in Go |

### 5. Rust Examples

| Directory | NPU platform | Runtime / framework | Description |
|-----------|--------------|---------------------|-------------|
| [rust_ort](rust_ort/) | Generic (NPU EP) | ort | ONNX Runtime Rust bindings with the NPU execution provider |

### 6. Java Examples

| Directory | NPU platform | Runtime / framework | Description |
|-----------|--------------|---------------------|-------------|
| [java_onnxruntime](java_onnxruntime/) | Generic (NPU EP) | onnxruntime-java | ONNX Runtime in Java with the NPU execution provider |
| [java_djl](java_djl/) | Multi-platform (NPU) | Deep Java Library | DJL unified loading with an NPU backend |

### 7. C# (.NET) Examples

| Directory | NPU platform | Runtime / framework | Description |
|-----------|--------------|---------------------|-------------|
| [csharp_onnxruntime](csharp_onnxruntime/) | Generic (NPU EP) | Microsoft.ML.OnnxRuntime | ONNX Runtime in .NET with the NPU execution provider |

### 8. JavaScript / Node.js Examples

| Directory | NPU platform | Runtime / framework | Description |
|-----------|--------------|---------------------|-------------|
| [node_onnxruntime](node_onnxruntime/) | Generic (NPU EP) | onnxruntime-node | ONNX Runtime in Node.js with the NPU execution provider |
| [node_webnn](node_webnn/) | Generic (WebNN) | WebNN API | WebNN NPU backend inference |

## Usage

1. Enter the target subdirectory and inspect the language/platform `main` file and dependency manifest.
2. Replace the `TODO` placeholders with the actual model path, input/output names, input dimensions, class counts, quantization parameters, and NPU device id.
3. Prepare the input images and model files (some platforms require converting the model to an NPU-specific format with the official toolchain first), then build and run per the directory instructions (Python `requirements.txt`, C++ `CMakeLists.txt`, Go `go.mod`, Rust `Cargo.toml`, Java `pom.xml`, C# `.csproj`, Node `package.json`).
