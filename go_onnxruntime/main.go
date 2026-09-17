// FasterEdge 开源项目 · https://github.com/FasterEdge · https://gitee.com/FasterEdge
// ONNX Runtime Go 推理示例（NPU 执行提供程序）
// 动态参数均用注释占位，按实际模型修改

package main

import (
	"fmt"
	"log"
	"time"

	ort "github.com/yalue/onnxruntime_go"
)

func main() {
	// ===== 动态参数（按实际模型修改）=====
	modelPath := "model.onnx" // TODO: 替换为 .onnx 模型路径

	// 输入/输出 shape 与名字按模型修改
	inputShape := ort.NewShape(1, 3, 640, 640)
	inputTensor, err := ort.NewEmptyTensor[float32](inputShape)
	if err != nil {
		log.Fatal(err)
	}
	defer inputTensor.Destroy()

	// TODO: 填充输入数据（读图、预处理 -> CHW）
	// data := inputTensor.GetData()

	options, err := ort.NewSessionOptions()
	if err != nil {
		log.Fatal(err)
	}
	defer options.Destroy()
	// TODO: 追加 NPU 执行提供程序（QNN/OpenVINO 等），否则回退 CPU

	session, err := ort.NewAdvancedSession(modelPath,
		[]string{"images"}, []string{"output"}, // TODO: 按输入/输出名修改
		nil, options, nil)
	if err != nil {
		log.Fatal(err)
	}
	defer session.Destroy()

	// 预热
	for i := 0; i < 3; i++ {
		if _, err = session.Run([]string{"images"}, []*ort.Tensor[float32]{inputTensor}); err != nil {
			log.Fatal(err)
		}
	}

	start := time.Now()
	if _, err = session.Run([]string{"images"}, []*ort.Tensor[float32]{inputTensor}); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("inference time: %v\n", time.Since(start))

	// TODO: 读取输出张量
}