# rime-profile

ObjectNotFound的Rime输入法配置

## 特点

- 包含两个输入法方案
  - 小鹤拼音 + [EasyEN](https://github.com/BlindingDark/rime-easy-en) 双语输入
  - 基于[JmdictFurigana](https://github.com/Doublevil/JmdictFurigana)的日语输入 
- 拼音输入法加入 [中文维基](https://github.com/felixonmars/fcitx5-pinyin-zhwiki)、[萌娘百科](https://github.com/outloudvi/mw2fcitx)词库，同时包含自定义流行语词库

## 配置存放位置

```text
Weasel (Windows)：％APPDATA％\Rime
trime (Android): /sdcard/rime
ibus-rime (Linux): ~/.config/ibus/rime
fctix5-rime (Linux)：~/.local/share/fctix5/rime
iRime (iOS): 使用内置 Web 服务器访问
```

## 使用方法

- 安装过程可能涉及 luna_pinyin.extended.dict.yaml 的构建（Build），请确保预留 2GB RAM（仅重新部署过程中需要）和 0.5GB 存储空间
- 下载客户端并安装
- Clone 项目（推荐使用 `--depth=1` 以节省网络流量和存储空间），将Repo内文件覆盖到配置文件夹内。提示文件被占用则可以直接 Kill 所有客户端进程
- 按需编辑 `installation.yaml`
- 重新启动输入法客户端，执行重新部署
- 输入法方案选择“朙月拼音”即可使用
- 如果需要制作自己的词库，**utils/** 内的脚本兴许有所帮助
