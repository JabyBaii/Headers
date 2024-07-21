#!/bin/bash

TAG=`git rev-parse --short HEAD`
DATE=`date +%Y-%m-%d_%H_%M_%S`
VERSION=${TAG}-${DATE}

Git_URL=`git remote -v`
IMAGE_NAME=`echo ${Git_URL} | awk -F ".git" '{print $2}' | awk -F "/" '{print $3}'`
echo $IMAGE_NAME
echo $VERSION

docker build -t ${IMAGE_NAME}:${VERSION} .
#docker push registry.cn-hangzhou.aliyuncs.com/myserver-io/tomcat-app1:$1


cd ./deployfiles

docker-compose down

sed -i "s/image: .*/image: ${IMAGE_NAME}:${VERSION}/g" docker-compose.yml

docker-compose up -d

