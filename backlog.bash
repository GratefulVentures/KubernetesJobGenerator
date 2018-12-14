#!/usr/bin/env bash
for filename in /Users/njohnson/PycharmProjects/GenerateConfigs/ad-manager/bid-landscape/*.yaml
do
kubectl create -f ${filename};
sleep 2;
done
