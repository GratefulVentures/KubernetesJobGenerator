#!/usr/bin/env bash
for filename in ./ga/daily/*.yaml
do
kubectl create -f ${filename};
sleep 2;
done