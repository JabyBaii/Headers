#!/bin/bash

TAG=`git rev-parse --short HEAD`
DATE=`date +%Y-%m-%d_%H_%M_%S`
VERSION=${TAG}-${DATE}

Git_URL=`git remote -v`
IMAGE_NAME=`echo ${Git_URL} | awk -F ".git" '{print $2}' | awk -F "/" '{print $3}' | tr 'A-Z' 'a-z'`
echo $IMAGE_NAME
echo $VERSION

cd ./deployfiles

echo "开始制作镜像...."
docker build -t ${IMAGE_NAME}:${VERSION} . -f Dockerfile.python310
#docker push registry.cn-hangzhou.aliyuncs.com/myserver-io/tomcat-app1:$1

echo "停止原有服务...."
docker-compose down

sed -i "s/image: .*/image: ${IMAGE_NAME}:${VERSION}/g" docker-compose.yml

echo "启动新版本...."
docker-compose up -d

