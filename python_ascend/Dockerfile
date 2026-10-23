# FasterEdge 开源项目 - Github: https://github.com/FasterEdge - Gitee: https://gitee.com/FasterEdge
# 华为昇腾 Ascend NPU 推理容器模板（CANN pyACL）
#
# 说明：实际 NPU 推理需基于官方 CANN 镜像（ascendai/cann）并挂载 NPU 设备，例如：
#   docker run --device /dev/davinci0 --device /dev/davinci_manager \
#     --device /dev/devmm_svm --device /dev/hisi_hdc \
#     -v /usr/local/Ascend/driver:/usr/local/Ascend/driver ascendai/cann:<version>
#
# 本 Dockerfile 以公共 Python 镜像为模板，演示示例代码的打包方式。

FROM python:3.14-slim

COPY ./requirements.txt /home
RUN pip install --no-cache-dir -r /home/requirements.txt

WORKDIR /home
COPY main.py /home/main.py

CMD ["python", "main.py"]
