#!/bin/bash
HOST=http://127.0.0.1:8093
# 测试通过 current_app 间接使用 db
echo -e "1. get models with flask by current_app:"
curl "$HOST/bp1/models"
echo -e "\n2. create async task to trigger task1:"
result_url=$(curl -XPOST -H 'Content-Type: application/json' -d'{"a": 1, "b":2}' $HOST/bp1/add 2>&1|grep -Po 'http[^"]+')
echo $result_url

echo -e "\n3. get models with celery of async task result by current_app:"
for i in {1..3}; do
    echo -e "\nloop ${i}:"
    curl $result_url
    sleep 5
done


# 测试直接从 models 中导入 db
echo -e "4. get models with flask by direct import:"
curl "$HOST/bp2/models"
echo -e "\n5. create async task to trigger task2:"
result_url=$(curl -XPOST -H 'Content-Type: application/json' -d'{"a": 1, "b":2}' $HOST/bp2/add 2>&1|grep -Po 'http[^"]+')
echo $result_url

echo -e "\n6. get models with celery of async task result by direct import:"
for i in {1..3}; do
    echo -e "\nloop ${i}:"
    curl $result_url
    sleep 5
done

echo test finished