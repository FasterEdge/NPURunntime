cmake_minimum_required(VERSION 3.15)
project(cpp_ascend)

# 需先安装 CANN 工具链并设置 Ascend 环境变量
add_executable(main main.cc)
# target_link_libraries(main ascendcl acl_op_compiler)  # TODO: 按 CANN 构建产物调整