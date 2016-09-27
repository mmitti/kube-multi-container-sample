# kube-multi-container-sample
Kubernetes 1Pod内で複数のコンテナを動かすサンプルです。

## 使い方
```
kubectl create -f test-db-viewer.yaml
```

そのご
http://kubernetes masterのIP:kubernetes APIのポート番号/api/v1/proxy/namespaces/default/services/test-db-viewer:5000  
にアクセスすれば動きます。

## アクセスした画面について
![](https://raw.githubusercontent.com/mmitti/kube-multi-container-sample/master/img.PNG "サンプル")

## test-db-viewer
