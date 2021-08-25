# vpsthings

## 性能测试
### unixbench
```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/unixbench.sh
chmod +x unixbench.sh
./unixbench.sh
```
**特点**
- Dhrystone 2 using register variables
此项用于测试 string handling，因为没有浮点操作，所以深受软件和硬件设计（hardware and software design）、编译和链接（compiler and linker options）、代码优化（code optimazaton）、对内存的cache（cache memory）、等待状态（wait states）、整数数据类型（integer data types）的影响。
- Double-Precision Whetstone
这一项测试浮点数操作的速度和效率。这一测试包括几个模块，每个模块都包括一组用于科学计算的操作。覆盖面很广的一系列 c 函数：sin，cos，sqrt，exp，log 被用于整数和浮点数的数学运算、数组访问、条件分支（conditional branch）和程序调用。此测试同时测试了整数和浮点数算术运算。
- Execl Throughput
此测试考察每秒钟可以执行的 execl 系统调用的次数。 execl 系统调用是 exec 函数族的一员。它和其他一些与之相似的命令一样是 execve（） 函数的前端。
- File copy
测试从一个文件向另外一个文件传输数据的速率。每次测试使用不同大小的缓冲区。这一针对文件 read、write、copy 操作的测试统计规定时间（默认是 10s）内的文件 read、write、copy 操作次数。
- Pipe Throughput
管道（pipe）是进程间交流的最简单方式，这里的 Pipe throughtput 指的是一秒钟内一个进程可以向一个管道写 512 字节数据然后再读回的次数。需要注意的是，pipe throughtput 在实际编程中没有对应的真实存在。
- Pipe-based Context Switching
这个测试两个进程（每秒钟）通过一个管道交换一个不断增长的整数的次数。这一点很向现实编程中的一些应用，这个测试程序首先创建一个子进程，再和这个子进程进行双向的管道传输。
- Process Creation
测试每秒钟一个进程可以创建子进程然后收回子进程的次数（子进程一定立即退出）。process creation 的关注点是新进程进程控制块（process control block）的创建和内存分配，即一针见血地关注内存带宽。一般说来，这个测试被用于对操作系统进程创建这一系统调用的不同实现的比较。
- System Call Overhead
测试进入和离开操作系统内核的代价，即一次系统调用的代价。它利用一个反复地调用 getpid 函数的小程序达到此目的。
- Shell Scripts
测试一秒钟内一个进程可以并发地开始一个 shell 脚本的 n 个拷贝的次数，n 一般取值 1，2，4，8。（我在测试时取 1， 8）。这个脚本对一个数据文件进行一系列的变形操作（transformation）。

### bench

```
wget -qO- bench.sh | bash
curl -Lso- bench.sh | bash
wget -qO- 86.re/bench.sh | bash
curl -so- 86.re/bench.sh | bash
```

**特点**

- 显示当前测试的各种系统信息；
- 取自世界多处的知名数据中心的测试点，下载测试比较全面；
- 支持 IPv6 下载测速；
- IO 测试三次，并显示平均值



### superbench

```
wget -qO- --no-check-certificate https://raw.githubusercontent.com/oooldking/script/master/superbench.sh | bash
或者
wget -qO- sb.oldking.net | bash
 
全面速度测试
bash <(curl -Lso- https://git.io/superspeed)
或者
wget git.io/superspeed.sh
bash superspeed.sh
```

在bench基础上加入了独服通电时间，服务器虚拟化架构等内容

**特点**

- 改进了显示的模式，基本参数添加了颜色，方面区分与查找。
- I/O测试，更改了原来默认的测试的内容，采用小文件，中等文件，大文件，分别测试IO性能，然后取平均值。

- 速度测试替换成了 Superspeed 里面的测试，第一个默认节点是，Speedtest 默认，其他分别测试到中国电信，联通，不同地区的速度。

### LemonBenchIntl 

```
curl -fsL https://ilemonra.in/LemonBenchIntl | bash -s fast
curl -fsL https://ilemonra.in/LemonBenchIntl | bash -s full
```

**特点**

- 服务器基础信息 (CPU信息/内存信息/Swap信息/磁盘空间信息/网络信息等)

- 流媒体解锁测试 (目前支持HBO Now/动画疯/B站港澳台/B站台湾限定)

- 系统性能测试 (CPU/内存/磁盘)

- Speedtest网速测试(本地到最近源及国内各地域不同线路的网速)

- 路由追踪测试 (追踪到国内和海外不同线路的路由信息)

### 91yun

```
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/91yuntest/master/test.sh && bash test.sh -i "io,bandwidth,chinabw,download,traceroute,backtraceroute,allping"
或者
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/91yuntest/master/test.sh && bash test.sh -i "io,bandwidth,chinabw,download,traceroute,backtraceroute,allping,gotoping,benchtest"
```



**特点**

- IO测试（通过DD命令来测试服务器的平均IO水平）
- 带宽测试（使用speedtest来测试服务器的上传和下载带宽）
- SpeedTest国内节点（测试使用speedtest来测试到国内节点的带宽和延迟）
- 下载测试（使用wget来测试到世界各地的下载速度，如果服务器带宽小于10M的话谨慎使用）
- 路由测试（从国内部分节点到测试服务器的路由线路）
- 回程路由（测试测试服务器到国内部分节点的回程路由线路）
- 全国Ping测试（全国各地到测试服务器的Ping值）
- 国外Ping测试（测试服务器到日韩美欧等地域的ping值）
- UnixBench跑分测试（该测试耗时将近1小时，并会跑满CPU，请谨慎测试）

### 参考

- https://vave.men/vpsjaoben.html

## 流媒体测试
- `bash <(curl -L -s https://raw.githubusercontent.com/lmc999/RegionRestrictionCheck/main/check.sh)`
- `bash <(curl -sSL "https://github.com/CoiaPrant/MediaUnlock_Test/raw/main/check.sh")`

## Buyvm

- 存储块监控：https://buyvm.qixi.me/
- 卢森堡机房抗投诉、无视DMCA版权，纽约、拉斯维加斯机房允许跑PT
- 支付宝付款通过加拿大元 (2美元=> 2加拿大元=>10.38人民币) 结算
- AMD Ryzen 3900X处理器，无限流量
- 可挂载存储块，1.25美元/256GB

### 中文乱码

- `locale-gen zh_CN.UTF-8`
- `/etc/default/locale`加入配置信息

```
LANG=zh_CN.UTF-8
LC_CTYPE="zh_CN.UTF-8"
LC_NUMERIC="zh_CN.UTF-8"
LC_TIME="zh_CN.UTF-8"
LC_COLLATE="zh_CN.UTF-8"
LC_MONETARY="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
LC_PAPER="zh_CN.UTF-8"
LC_NAME="zh_CN.UTF-8"
LC_ADDRESS="zh_CN.UTF-8"
LC_TELEPHONE="zh_CN.UTF-8"
LC_MEASUREMENT="zh_CN.UTF-8"
LC_IDENTIFICATION="zh_CN.UTF-8"
LC_ALL=zh_CN.UTF-8
```

- `update-locale LANG=zh_CN.UTF-8`
- `reboot`

### 挂载存储块

- 查看现有存储块

```
$ ls /dev/disk/by-id/
ata-QEMU_DVD-ROM_QM00004  scsi-0BUYVM_SLAB_VOLUME-8601
```

- 格式化存储块

```
$ mkfs.ext4 -F /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-8601
```

- 创建文件夹

```
mkdir /sdb
```

- 挂载盘

```
mount -o discard,defaults /dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-8601 /sdb
```

- 开机自动挂载

```
echo '/dev/disk/by-id/scsi-0BUYVM_SLAB_VOLUME-8601 /sdb ext4 defaults,nofail,discard 0 0' | sudo tee -a /etc/fstab
```

## 硬盘扩展和同步

- rclone
- rsync： http://www.ruanyifeng.com/blog/2020/08/rsync.html



## 安全

- fail2ban：https://www.cnblogs.com/Narule/p/13040065.html

```
apt-get install -y fail2ban
systemctl start fail2ban
systemctl status fail2ban
systemctl enable fail2ban
vim /etc/fail2ban/jail.local
systemctl restart fail2ban
systemctl status fail2ban
fail2ban-client status sshd
```

