base_image_path=registry.cn-shanghai.aliyuncs.com/zhph-server

docker pull ghcr.io/1panel-dev/maxkb-vector-model:v1.0.1
docker pull ghcr.io/1panel-dev/maxkb-python-pg:python3.11-pg15.6
docker pull node:18-alpine3.18

docker tag ghcr.io/1panel-dev/maxkb-vector-model:v1.0.1 $base_image_path/maxkb-vector-model:v1.0.1
docker tag ghcr.io/1panel-dev/maxkb-python-pg:python3.11-pg15.6 $base_image_path/maxkb-python-pg:python3.11-pg15.6
docker tag node:18-alpine3.18 $base_image_path/node:18-alpine3.18

docker push $base_image_path/maxkb-vector-model:v1.0.1
docker push $base_image_path/maxkb-python-pg:python3.11-pg15.6
docker push $base_image_path/node:18-alpine3.18