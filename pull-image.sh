base_image_path=registry.cn-shanghai.aliyuncs.com/zhph-server

docker pull $base_image_path/maxkb-vector-model:v1.0.1
docker pull $base_image_path/maxkb-python-pg:python3.11-pg15.6
docker pull $base_image_path/node:18-alpine3.18

docker tag $base_image_path/maxkb-vector-model:v1.0.1 ghcr.io/1panel-dev/maxkb-vector-model:v1.0.1 
docker tag $base_image_path/maxkb-python-pg:python3.11-pg15.6 ghcr.io/1panel-dev/maxkb-python-pg:python3.11-pg15.6 
docker tag $base_image_path/node:18-alpine3.18 node:18-alpine3.18
