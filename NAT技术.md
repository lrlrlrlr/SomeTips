# 起因
---
因为出于安全性的考虑, 公司的内网不对外开放, 但是有时候需要在外网访问内网。那么，如何才能在家舒服的使用公司内网呢？:smile: 


# 经过
---
  比较粗浅的方法是使用Teamviewer软件直接远程控制在公司内网下的机器使用浏览器进行操作。然而我并不满足于这种低级的方式，我想通过设置代理这样的方式来直接连接内网；本以为使用shadowsocks这样的vpn软件就能实现，但是发现这些软件搭建vpn统统都要“公网IP+端口”来实现，然而我并不能操作路由器，也不认识公司的网管，无法在路由器上设置`端口转发`，所以不能将VPN搭建起来。 
  
# 结果
---
  这里把尝试过的所有方法列出来以供参考:
  *使用teamviewer直接控制内网机器打开内网
    blab
  *搭建vpn或者代理
    常见搭建vpn和代理的方法是使用shadowsocks和ccproxy这种软件，但是在尝试过程中，我发现他们需要的
  *使用teamviewer的vpn功能
    blabla
  *其他方法: 肯定还有更好的方法~
   
    
  


# reference:  
---
* 基础知识:  
  * [Proxy][Proxy]
  * [NAT][NAT]

* 解决问题参考:   
  * [在家访问公司内网代理设置方法][在家访问公司内网代理设置方法]
  * [Setup & Configure VPN with Teamviewer][Setup & Configure VPN with Teamviewer]


--------------------------------
[NAT]:https://en.wikipedia.org/wiki/Network_address_translation
[Proxy]:https://en.wikipedia.org/wiki/Proxy_server "代理"

[在家访问公司内网代理设置方法]:https://zhidao.baidu.com/question/540121234.html "TeamViewer和ccproxy"
[Setup & Configure VPN with Teamviewer]:https://www.youtube.com/watch?v=DthTedu0KgI

[知乎搜索"内网穿透"]:https://www.zhihu.com/search?type=content&q=%E7%A9%BF%E9%80%8F%E5%86%85%E7%BD%91
[n2n 内网穿透折腾记]:https://zhuanlan.zhihu.com/p/25344743
