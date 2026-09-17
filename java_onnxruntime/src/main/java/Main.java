// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// ONNX Runtime Java 推理示例（NPU 执行提供程序）
// 动态参数均用注释占位，按实际模型修改

import ai.onnxruntime.OnnxTensor;
import ai.onnxruntime.OrtEnvironment;
import ai.onnxruntime.OrtSession;
import ai.onnxruntime.OrtSession.Result;
import ai.onnxruntime.OrtSession.SessionOptions;

public class Main {
    public static void main(String[] args) throws Exception {
        // ===== 动态参数（按实际模型修改）=====
        String modelPath = "model.onnx";       // TODO: 替换为你的 .onnx 模型路径
        long[] inputShape = {1L, 3L, 640L, 640L};  // TODO: 按模型输入修改
        String inputName = "images";           // TODO: 按模型输入名修改

        try (OrtEnvironment env = OrtEnvironment.getEnvironment()) {
            SessionOptions opts = new SessionOptions();
            // TODO: 追加 NPU 执行提供程序（opts.addNnapi() 或 QNN/OpenVINO EP）

            try (OrtSession session = env.createSession(modelPath, opts)) {
                // TODO: 填充实际输入数据（读图、预处理 -> CHW）
                float[] inputData = new float[1 * 3 * 640 * 640];

                try (OnnxTensor input = OnnxTensor.createTensor(env,
                        java.nio.FloatBuffer.wrap(inputData), inputShape)) {
                    // 预热
                    for (int i = 0; i < 3; i++) {
                        try (Result r = session.run(java.util.Map.of(inputName, input))) {
                            // discard
                        }
                    }

                    long start = System.nanoTime();
                    try (Result result = session.run(java.util.Map.of(inputName, input))) {
                        long ms = (System.nanoTime() - start) / 1_000_000;
                        System.out.println("inference time: " + ms + " ms");
                        // TODO: 解析 result.get("output0") 输出张量
                    }
                }
            }
        }
    }
}