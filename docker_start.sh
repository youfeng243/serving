#!/usr/bin/env bash


docker stop tf_server
docker rm tf_server
docker run -idt -p 8501:8501 -v "$(pwd)/tensorflow_serving/servables/tensorflow/testdata/:/models/"  --name="tf_server"   tensorflow/serving --model_config_file=/models/models.config --model_config_file_poll_wait_seconds=60
