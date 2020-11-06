cmake_minimum_required(VERSION 3.15)
project(day03)

set(CMAKE_CXX_STANDARD 14)

add_executable(day03 main.cpp)

# 登记函数的程序
add_executable(01_function_01_main 01_function/01_main.cpp)
add_executable(01_function_02_main 01_function/02_main.cpp)
add_executable(01_function_03_main 01_function/03_main.cpp)

#指针
add_executable(02_pointer_01_main 02_pointer/01_main.cpp)
add_executable(02_pointer_02_main 02_pointer/02_main.cpp)
add_executable(02_pointer_03_main 02_pointer/03_main.cpp)
add_executable(02_pointer_04_main 02_pointer/04_main.cpp)
add_executable(02_pointer_05_main 02_pointer/05_main.cpp)
add_executable(02_pointer_06_main 02_pointer/06_main.cpp)
add_executable(02_pointer_07_main 02_pointer/07_main.cpp)

# 引用
add_executable(03_reference_01_main 03_reference/01_main.cpp)
add_executable(03_reference_02_main 03_reference/02_main.cpp)
add_executable(03_reference_03_main 03_reference/03_main.cpp)