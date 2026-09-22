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
	inputName := "images"   // TODO: 按模型输入名修改
	outputName := "output0" // TODO: 按模型输出名修改

	if err := ort.InitializeEnvironment(); err != nil {
		log.Fatal(err)
	}
	defer ort.DestroyEnvironment()

	// TODO: 填充输入数据（读图、预处理 -> CHW）
	inputData := make([]float32, 1*3*640*640)
	inputTensor, err := ort.NewTensor(inputShape, inputData)
	if err != nil {
		log.Fatal(err)
	}
	defer inputTensor.Destroy()

	// TODO: 输出 shape 用 nil 自动推断，按模型实际输出名修改
	outputTensor, err := ort.NewEmptyTensor[float32](nil)
	if err != nil {
		log.Fatal(err)
	}
	defer outputTensor.Destroy()

	options, err := ort.NewSessionOptions()
	if err != nil {
		log.Fatal(err)
	}
	defer options.Destroy()
	// TODO: 追加 NPU 执行提供程序（QNN/OpenVINO 等），否则回退 CPU

	session, err := ort.NewAdvancedSession(modelPath,
		[]string{inputName}, []string{outputName},
		[]ort.Value{inputTensor}, []ort.Value{outputTensor}, options)
	if err != nil {
		log.Fatal(err)
	}
	defer session.Destroy()

	// 预热
	for i := 0; i < 3; i++ {
		if err := session.Run(); err != nil {
			log.Fatal(err)
		}
	}

	start := time.Now()
	if err := session.Run(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("inference time: %v\n", time.Since(start))

	// TODO: 读取 outputTensor.GetData() 并后处理
}
