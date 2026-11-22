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

	// 用 DynamicAdvancedSession 而非 AdvancedSession：输出 shape 由 ORT 分配，
	// 不需要预先知道（NewEmptyTensor 不接受 nil shape，会返回
	// "Invalid tensor shape: The shape has no dimensions"）。实跑于 yolov5n.onnx
	// 验证通过，见 matrix.json 的 evidence 字段。
	options, err := ort.NewSessionOptions()
	if err != nil {
		log.Fatal(err)
	}
	defer options.Destroy()
	// TODO: 追加 NPU 执行提供程序（QNN/OpenVINO 等），否则回退 CPU

	session, err := ort.NewDynamicAdvancedSession(modelPath,
		[]string{inputName}, []string{outputName}, options)
	if err != nil {
		log.Fatal(err)
	}
	defer session.Destroy()

	// 输出张量传 nil，ORT 会自动分配并在 Run 后填入切片
	outputs := []ort.Value{nil}
	runOnce := func() error {
		return session.Run([]ort.Value{inputTensor}, outputs)
	}

	// 预热
	for i := 0; i < 3; i++ {
		if err := runOnce(); err != nil {
			log.Fatal(err)
		}
	}

	start := time.Now()
	if err := runOnce(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("inference time: %v\n", time.Since(start))

	// TODO: 后处理 outputs[0]（需按类型断言为 *ort.Tensor[float32] 后读 GetData()）
	if out, ok := outputs[0].(interface{ GetShape() ort.Shape }); ok {
		fmt.Printf("output shape: %v\n", out.GetShape())
	}
	for _, o := range outputs {
		if o != nil {
			defer o.Destroy()
		}
	}
}
