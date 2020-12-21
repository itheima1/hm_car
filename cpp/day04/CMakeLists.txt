cmake_minimum_required(VERSION 3.15)
project(day04)

set(CMAKE_CXX_STANDARD 14)

add_executable(day04 main.cpp)

# 引用
add_executable(01_reference_01_main 01_reference/01_main.cpp)
add_executable(01_reference_02_main 01_reference/02_main.cpp)

# 面向对象
add_executable(02_oop_01_main 02_oop/01_main.cpp)
add_executable(02_oop_02_main 02_oop/02_main.cpp)
add_executable(02_oop_03_main 02_oop/03_main.cpp)
add_executable(02_oop_04_main 02_oop/04_main.cpp)
add_executable(02_oop_05_main 02_oop/05_main.cpp)
add_executable(02_oop_06_main 02_oop/06/main.cpp 02_oop/06/stu.cpp)
add_executable(02_oop_07_main 02_oop/07_main.cpp)
add_executable(02_oop_08_main 02_oop/08_main.cpp)
add_executable(02_oop_09_main 02_oop/09_main.cpp)
add_executable(02_oop_10_main 02_oop/10_main.cpp)
add_executable(02_oop_11_main 02_oop/11_main.cpp)
add_executable(02_oop_12_main 02_oop/12_main.cpp)
add_executable(02_oop_13_main 02_oop/13_main.cpp)

add_executable(07_main 02_oop/07/main.cpp)