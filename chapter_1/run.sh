#!/bin/bash
docker build -t chapter_1_homlflow .
docker run -p 8888:8888 -p 5000:5000 -v $(pwd):/home/jovyan/ -it chapter_1_homlflow

