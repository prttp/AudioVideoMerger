cmake_minimum_required(VERSION 3.15)
project(AudioVideoMerger)

find_package(ffmpeg REQUIRED)

message("Building with CMake version: ${CMAKE_VERSION}")

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} ffmpeg::ffmpeg)