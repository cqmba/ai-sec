## Set up a VM Software
Either use VMWare or Virtualbox whichever you are more familiar with 

## Set up SecurityOnion
Download the ISO from the git repository (Just read the README for instruction): 
* https://github.com/Security-Onion-Solutions/security-onion/blob/master/Verify_ISO.md

Follow the Video for a minimal Set up: https://youtu.be/RAV17X9YJuY

However a one differences to the instructions of the video. Don't use a virtual network but a HOST-ONLY network for the second network adapter (only use a virtual network if you need a connection between two VMS)

Another difference is that you want to have Security Onion to listen to your second ethernet connection instead of the first (in my case enp0s8 instead of enp0s3), basically make security onion listen to the HOST-ONLY connection instead of the NAT network. (IF the host only adapter is your first adapter then use that one instead of course)


## Prope with nmap
After installing and doing the minimal setup you can start to run nmap for a prope. (Also maybe set a safe point so you don't have to this all again in case you mess up)

get the ip address of your machine: use `ifconfig` and look through the network adapter for your second connection (eth08 in my case).

To test if you can get a connection from your host machine try ping that ip address (in my case this was `192.168.56.102`).

Start Squil and use the login data that you used in `so-setup-minimal`

after that simply run `nmap -T4 -A -v 192.168.56.102` for a prope 

## Miscellaneous

It can be that you have to enable an exception into your firewall, just set it so that both the `Ethernet-Adapter VirtualBox Host-Only Network` and the actual machine are allowed to get through.

Google how to enable exceptions for that.

To disable the firewall on SecurityOnion just run `sudo ufw disable`
