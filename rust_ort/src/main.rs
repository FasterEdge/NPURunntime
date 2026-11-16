// FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
// ONNX Runtime Rust 推理示例（NPU 执行提供程序）
// 动态参数均用注释占位，按实际模型修改

use std::time::Instant;

fn main() -> ort::Result<()> {
    // ===== 动态参数（按实际模型修改）=====
    let model_path = "model.onnx"; // TODO: 替换为 .onnx 模型路径

    let environment = ort::init().build()?;
    let session = ort::session::Session::builder(&environment)?
        // TODO: 追加 NPU 执行提供程序（QNN/OpenVINO），例如
        // .with_execution_providers([ort::execution_providers::QNNExecutionProvider::default().build()])?
        .commit_from_file(model_path)?;

    // TODO: 填充输入数据（读图、预处理 -> CHW），构造 ort::value::Tensor
    // let input = ndarray::Array4::<f32>::zeros((1, 3, 640, 640));

    // 预热
    // for _ in 0..3 {
    //     let _ = session.run(ort::inputs![
    //         "images" => ort::value::TensorRef::from_array_view(input.view())?
    //     ])?;
    // }

    let start = Instant::now();
    // let output = session.run(ort::inputs![
    //     "images" => ort::value::Tensor::from_array(input)?
    // ])?;
    println!("inference time: {:?}", start.elapsed());

    // TODO: 解析输出 output["output"]
    Ok(())
}
