#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tensorflow_serving.apis import model_management_pb2
from tensorflow_serving.apis import model_service_pb2_grpc
from tensorflow_serving.config import model_server_config_pb2

"""
热更新代码示例,能够动态新增模型
"""

import grpc


def run():
    channel = grpc.insecure_channel('192.168.199.198:8500')
    stub = model_service_pb2_grpc.ModelServiceStub(channel)
    # message ReloadConfigRequest
    request = model_management_pb2.ReloadConfigRequest()
    model_server_config = model_server_config_pb2.ModelServerConfig()

    # message ModelConfigList
    config_list = model_server_config_pb2.ModelConfigList()

    print(config_list)

    ####try to add
    one_config = config_list.config.add()
    one_config.name = "saved_model_half1"
    one_config.base_path = "/models/saved_model_half_plus_two_cpu"
    one_config.model_platform = "tensorflow"

    one_config = config_list.config.add()
    one_config.name = "saved_model_half2"
    one_config.base_path = "/models/saved_model_half_plus_two_cpu"
    one_config.model_platform = "tensorflow"

    one_config = config_list.config.add()
    one_config.name = "saved_model_half3"
    one_config.base_path = "/models/saved_model_half_plus_two_cpu"
    one_config.model_platform = "tensorflow"

    one_config = config_list.config.add()
    one_config.name = "saved_model_half4"
    one_config.base_path = "/models/saved_model_half_plus_two_cpu"
    one_config.model_platform = "tensorflow"

    # one_config = config_list.config.add()
    # one_config.name = "saved_model_half5"
    # one_config.base_path = "/models/saved_model_half_plus_two_cpu_bak"
    # one_config.model_platform = "tensorflow"

    model_server_config.model_config_list.CopyFrom(config_list)  # one of

    request.config.CopyFrom(model_server_config)

    print(request.IsInitialized())
    print(request.ListFields())

    response = stub.HandleReloadConfigRequest(request, 10)
    if response.status.error_code == 0:
        print("reload sucessfully")
    else:
        print("reload error!")
        print(response.status.error_code)
        print(response.status.error_message)


if __name__ == '__main__':
    run()
