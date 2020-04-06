rest_api汇总
-----------------
### 查看meta信息接口
curl http://localhost:8501/v1/models/saved_model_half3/metadata

### 预测接口
* curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://localhost:8501/v1/models/saved_model_half3:predict
* curl -d '{"instances": [1.0, 2.0, 5.0]}' -X POST http://localhost:8501/v1/models/saved_model_half3/versions/123:predict


### [rest接口说明文档链接](https://www.jianshu.com/p/a9dbf1e63c88?utm_source=oschina-app)
```http request
POST http://host:port/<URI>:<VERB>
URI: /v1/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]
VERB: classify|regress|predict
```
请求URL的示例:
```http request
http://host:port/v1/models/iris:classify
http://host:port/v1/models/mnist/versions/314:predict
```