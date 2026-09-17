cmake_minimum_required(VERSION 3.15)
project(cpp_openvino_npu)

find_package(OpenVINO REQUIRED)
add_executable(main main.cc)
target_link_libraries(main openvino::runtime)