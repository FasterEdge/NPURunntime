cmake_minimum_required(VERSION 3.15)
project(cpp_ncnn)

# 需先构建/安装 NCNN 库
add_executable(main main.cc)
# target_link_libraries(main ncnn)  # TODO: 按 NCNN 构建产物调整