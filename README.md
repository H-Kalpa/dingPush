# 钉钉CS上线提醒

鉴于没有找到一个可以正常使用的CS上线提醒插件，于是决定自己动手丰衣足食。

核心代码位于Python文件中，其它通知平台可自行修改。

## 配置

修改`dingPush.cna`的路径，注意为绝对路径。

```
$cmd = 'python3 /opt/CobaltStrikeClient/csplugins/dingPush/dingPush.py' . ' --computername ' . $computerName . ' --internalip ' . $internalIP . ' --username ' . $userName;
```

修改`dingPush.py`的加签值和Webhook，可参考：[自定义机器人接入 - 钉钉开放平台](https://open.dingtalk.com/document/orgapp/custom-robot-access)

```
token = "xxx"  # 替换为您的钉钉机器人access_token
secret = "xxx"  # 替换为您的钉钉机器人密钥
```

其它配置自行探索。

## 使用

导入CS客户端即可。

## 参考文档

[自定义机器人安全设置 - 钉钉开放平台](https://open.dingtalk.com/document/robots/customize-robot-security-settings)