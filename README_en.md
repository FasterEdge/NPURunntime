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

## Verifiability Matrix (machine-readable)

The repository root `matrix.json` records the real verifiability state of every example, extracted from the
source code by a script — it is **not hand-written**:

```
python tools/gen_matrix.py            # re-extract and overwrite matrix.json
python tools/gen_matrix.py --check    # fail with exit code 1 if matrix.json disagrees with the source
python tools/verify_matrix.py         # really build + run the declared cases and write evidence back
python tools/verify_matrix.py --check # read-only check that the existing evidence still holds (no rerun, no write)
```

`--check` compares only the source facts that are independent of the toolchain and of the local Python
interpreter (unresolved TODOs, whether an inference call exists, model formats, entry file, missing-dependency
list, bundled model files). It deliberately skips `status`, `compile_check`, and `evidence` — those depend on
whether g++ / node / gofmt / dotnet / cargo and the ONNX Runtime shared library are installed locally, so
cross-machine comparison produces false failures — and it skips `environment` / `summary` (local Python
version and status counts).

`evidence.command` has local absolute paths replaced with placeholders (`<repo>/`, `<tmp>`,
`<home>`) when the evidence is written back, keeping only the information that matters (“which
temp directory”). The matrix is committed, so baking in `C:\Users\<user>\...` would make it
impossible for anyone else to reproduce the command and would leak local details into the
repository. `evidence.output_tail` is the tail of the output from that very run; non-ASCII text is
decoded strictly as UTF-8 first and falls back to the local code page, so no U+FFFD ever lands in
the matrix.

Status definitions (exactly one of three; the decision rules are documented in the `tools/gen_matrix.py`
top docstring):

| Status | Meaning |
|--------|---------|
| `verified` | Real build + run driven by `tools/verify_matrix.py`; command and output recorded in the `evidence` field of `matrix.json` |
| `compilable` | Syntax/compile check passed (Python `py_compile`-equivalent syntax check, Go `gofmt -l`, JS `node --check`, C++ `g++ -fsyntax-only`, Java bare `javac` without classpath, Rust `cargo check --offline`, C# `dotnet build`), but the inference call has not executed (missing model or runtime) |
| `placeholder` | An unresolved `TODO` remains, the inference call is missing or commented out, or the syntax/compile check failed |

> **On "not pretending to run a real NPU"**: `status` only becomes `verified` after `tools/verify_matrix.py`
> has actually driven the example, and that script declares exactly one case (`go_onnxruntime`). So there are
> only two reproducible states in this repository:
>
> - After `python tools/gen_matrix.py` alone: `summary.verified == 0` and **all 29/29 examples are
>   `placeholder`** (`gen_matrix.py` never writes `verified` by itself).
> - After `python tools/verify_matrix.py`: `go_onnxruntime` is promoted to `verified` and the command plus
>   output are recorded in its `evidence` field. That case runs the **ONNX Runtime CPU execution provider
>   (not an NPU)**, borrowing `yolov5n.onnx` from the sibling repository ModelRunntime; this repository ships
>   no model files. The other 28 examples stay `placeholder`.
>
> **No NPU inference path has ever executed on this machine**: it has no Ascend / Rockchip / Qualcomm /
> Horizon / Cambricon NPU and no vendor SDKs such as CANN / RKNPU2 / SNPE / QNN / NeuroPilot / Core ML.
> `bundled_models` is an empty array for all 29 examples, i.e. the repository contains no loadable model file.
> The specific missing dependencies for each example are listed in the `missing_deps` field of `matrix.json`.
> This is not "unfinished" but an honest statement of the hardware boundary: **no hardware, no SDK, no claim
> of working**.
>
> On shell functions: the `run_inference` of `python_ascend` / `python_cambricon` / `python_executorch` /
> `python_horizon` / `python_mediatek` now always raises `NotImplementedError` and no longer returns
> `[]` / `None` — that would let `__main__` print "done 0 outputs" and exit with code 0, a fake success path.
> Accordingly `signals.shell_functions` is an empty array for all 29 examples (0 entries in total) and is no
> longer a decision signal. These examples remain `placeholder` because `signals.todo_lines` is non-empty
> (the inference body still carries TODOs) or `signals.live_inference_call_lines` is empty (no real inference
> call at all).

## Usage

1. Enter the target subdirectory and inspect the language/platform `main` file and dependency manifest.
2. Replace the `TODO` placeholders with the actual model path, input/output names, input dimensions, class counts, quantization parameters, and NPU device id.
3. Prepare the input images and model files (some platforms require converting the model to an NPU-specific format with the official toolchain first), then build and run per the directory instructions (Python `requirements.txt`, C++ `CMakeLists.txt`, Go `go.mod`, Rust `Cargo.toml`, Java `pom.xml`, C# `.csproj`, Node `package.json`).

> The Go examples depend on native C runtimes: `go_onnxruntime` requires the ONNX Runtime C shared library (use `ort.SetSharedLibraryPath` to point to it); `go_tflite` requires the TensorFlow Lite C API headers and `libtensorflowlite_c.so`, with `CGO_CFLAGS` / `CGO_LDFLAGS` set as documented upstream. These native libraries and model files are not bundled in this repository.
