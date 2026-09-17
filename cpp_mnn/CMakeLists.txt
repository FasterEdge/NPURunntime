cmake_minimum_required(VERSION 3.15)
project(cpp_mnn)

# 需先构建/安装 MNN 库
add_executable(main main.cc)
# target_link_libraries(main MNN)  # TODO: 按 MNN 构建产物调整