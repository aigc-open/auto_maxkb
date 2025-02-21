image_name=registry.cn-shanghai.aliyuncs.com/zhph-server/auto_maxkb:1.0

docker build -t $image_name . -f installer/Dockerfile
docker push $image_name