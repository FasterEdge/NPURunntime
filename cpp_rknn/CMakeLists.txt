cmake_minimum_required(VERSION 3.15)
project(cpp_rknn)

# 需先安装 RKNPU2 SDK（librknnrt.so）
add_executable(main main.cc)
# target_link_libraries(main rknnrt)  # TODO: 按 RKNPU2 构建产物调整