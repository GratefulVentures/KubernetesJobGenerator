#!/usr/bin/env bash
for filename in ./ad-manager/bid-landscape/*.yaml
do
kubectl create -f ${filename};
sleep 2;
done
