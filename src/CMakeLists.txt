cmake_minimum_required(VERSION 2.8.12)
project(UsingSharedLibConan CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_library(DATETIMELIB_LIBRARY NAMES datetimeutil)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
