cmake_minimum_required(VERSION 3.0)

project(UsingSharedLibConan)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} ./src/main.cpp)

target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
