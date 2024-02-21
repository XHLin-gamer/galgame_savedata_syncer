# galgame_savedata_syncer
<!-- ![はてな](hatena.jpg | width=100) -->
<p align="center">
<img src='hatena-modified.png' width=35%>
</p>



最近沉迷上了串流打galgame，在床上用手机玩真的很舒适，而且正好可以利用闲置的电脑。但是手动的同步笔电和串流服务器的存档文件实在太过于痛苦，于是就简单地写一个脚本，方便进行存档的同步。

## 使用方法
- 本脚本默认用户有python环境
- 你需要将设备部署于同一个网络环境下（windows的网上邻居可以相互访问），或者和使用Zerotier
- 在配置文件(config.py)中填写你需要同步的存档文件夹的路径，基本上双击进入存档文件夹，复制windows路径栏的内容即可
- 在需要进行同步的时候，运行sync.bat脚本 
  
----
## TODO

- [ ] 对配置文件进行修改，支持对电脑进行命名，配置游戏名称
- [ ] 以Windows托盘程序的形式适配GUI

----
<p align="center">
終わり
</p>
