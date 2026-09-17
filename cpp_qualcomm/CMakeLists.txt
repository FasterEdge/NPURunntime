cmake_minimum_required(VERSION 3.15)
project(cpp_qualcomm)

# 需先安装 Qualcomm SNPE/QNN SDK
add_executable(main main.cc)
# target_link_libraries(main SNPE QnnHtp)  # TODO: 按 SNPE/QNN SDK 调整