## Set up a VM Software
Either use VMWare or Virtualbox whichever you are more familiar with 

## Set up SecurityOnion
Download the ISO from the git repository (Just read the README for instruction): 
* https://github.com/Security-Onion-Solutions/security-onion/blob/master/Verify_ISO.md

Follow the Video for a minimal Set up: https://youtu.be/RAV17X9YJuY

However one difference to the instructions of the video. Don't use a virtual network but a HOST-ONLY network for the second network adapter (only use a virtual network if you need a connection between two VMS)

Another difference is that you want to have Security Onion to listen to your second ethernet connection instead of the first (in my case enp0s8 instead of enp0s3), basically make security onion listen to the HOST-ONLY connection instead of the NAT network. (IF the host only adapter is your first adapter then use that one instead of course)


## Prope with nmap
After installing and doing the minimal setup you can start to run nmap for a prope. (Also maybe set a safe point so you don't have to this all again in case you mess up)

get the ip address of your machine: use `ifconfig` and look through the network adapter for your second connection (enp0s8 in my case).

To test if you can get a connection from your host machine try ping that ip address (in my case this was `192.168.56.102`).

Start Squil and use the login data that you used in `so-setup-minimal`

after that simply run `nmap -T4 -A -v 192.168.56.102` for a prope 

## Miscellaneous

It can be that you have to enable an exception into your firewall, just set it so that both the `Ethernet-Adapter VirtualBox Host-Only Network` and the actual machine are allowed to get through.

Google how to enable exceptions for that.

To disable the firewall on SecurityOnion just run `sudo ufw disable`

The if config output of my security onion instance:

```
// NAT adapter connection
enp0s3    Link encap:Ethernet  HWaddr 08:00:27:26:66:e6  
          UP BROADCAST RUNNING NOARP PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:90 (90.0 B)
// HOST ONLY connection
enp0s8    Link encap:Ethernet  HWaddr 08:00:27:e4:34:1b  
          inet addr:192.168.56.102  Bcast:192.168.56.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fee4:341b/64 Scope:Link
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:2163 errors:0 dropped:0 overruns:0 frame:0
          TX packets:94 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:162457 (162.4 KB)  TX bytes:7565 (7.5 KB)

```
