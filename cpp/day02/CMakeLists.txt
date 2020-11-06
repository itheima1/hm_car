cmake_minimum_required(VERSION 3.15) # 要求cmake的最低版本是3.5
project(day02) # 表示工程名 |项目名

set(CMAKE_CXX_STANDARD 14) # 表示使用什么c++版本去编译咱们代码


# 创建一个可执行程序  ， 可执行的程序名叫做day02 , 根据main.cpp源文件来创建的。
add_executable(main main.cpp)


# 在这里登记所有的可执行程序。
#add_executable(01_loop_main  01_loop/main.cpp)

# 循环
add_executable(01_loop_01_main 01_loop/01_main.cpp)
add_executable(01_loop_02_main 01_loop/02_main.cpp)

# 数组
add_executable(02_array_01_main  02_array/01_main.cpp)
add_executable(02_array_02_main  02_array/02_main.cpp)
add_executable(02_array_03_main  02_array/03_main.cpp)
add_executable(02_array_04_main  02_array/04_main.cpp)

# 字符串
add_executable(03_str_01_main 03_str/01_main.cpp)

# vector
add_executable(04_vector_01_main 04_vector/01_main.cpp)
add_executable(04_vector_02_main 04_vector/02_main.cpp)
add_executable(04_vector_03_main 04_vector/03_main.cpp)

# function
add_executable(05_function_01_main  05_function/01_main.cpp)
add_executable(05_function_02_main  05_function/02_main.cpp)
add_executable(05_function_03_main  05_function/03_main.cpp)
add_executable(05_function_split_main 05_function/split/main.cpp 05_function/split/hello.cpp)
