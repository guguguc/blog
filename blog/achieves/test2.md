## 0x00 大纲

- 包管理器    pacman
- 打包
- 包描述文件  PKGBUILD
- 自动化打包  makepkg
- Example

## 0x01 Pacman

Pacman是Archlinux的包管理器。主要提供了安装，更新，卸载，等软件包管理的功能。Pacman使用C语言编写，其内部使用tar文件格式来进行打包。

**基本信息**

| 目录                  | 含义       |
| --------------------- | ---------- |
| /var/log/pacman.log   | 包安装日志 |
| /var/lib/pacman/local | 包安装信息 |
| /var/cache/pacman/pkg | 包缓存     |

**基本命令**

| 命令        | 含义                                         |
| ----------- | -------------------------------------------- |
| Pacman -S   | 安装软件包                                   |
| Pacman -Ss  | 搜索软件包                                   |
| Pacman -Syu | 升级所有已安装的包                           |
| Pacman -Sw  | 仅下载包                                     |
| Pacman -Scc | 清除所有包缓存                               |
| pacman -Sc  | 清除包缓存(除了已安装的)                     |
| Pacman -Rs  | 移除软件包                                   |
| Pacman -Si  | 查询包信息(描述，依赖，安装大小，构建日期等) |
| Pacman -Sii | 查询所有依赖此包的包                         |
| Pacman -Qi  | 查询本地包信息(全名)                         |
| Pacman -Qii | 本地查询，同-Sii                             |
| Pacman -Qs  | 同上(模糊匹配)                               |

**配置**

配置文件目录位于`/etc/pacman.conf`

## 0x0x2 打包

Pacman还提供了makepkg工具，通过PKGBUILD包描述文件来构建二进制包。测试成功之后，你也可以将你的包提交到AUR上。

基本流程如下：

0. 下载软件源代码(当然也可以是你的代码)并编译软件包
1. 创建PKGBUILD文件
2. 使用makepkg测试PKGBUILD有效性并构建本地包
3. 提交到AUR(可选)



## 参考

[1] https://jlk.fjfi.cvut.cz/arch/manpages/man/pacman.8
[2] https://wiki.archlinux.org/index.php/Pacman/Rosetta
[3] https://wiki.archlinux.org/index.php/Creating_packages
[4] https://jlk.fjfi.cvut.cz/arch/manpages/man/makepkg.8
