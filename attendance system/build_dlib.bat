@echo off
cd "C:\Python Programs\attendance system\.venv\Scripts\build"
cmake "..\dlib" -G "Visual Studio 16 2019" -A x64 -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1 -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=..\dlib\build\lib
