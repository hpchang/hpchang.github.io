Title: Construction on Windows 10
Date: 2017-09-06 00:00
Modified: 2017-11-21 00:00
Category: windows software
Tags: windows10, windows
Slug: rebuild-on-windows-10
lang: en
Authors: HP Chang
Summary: Note for install Bash, tools on Windows 10




Backup is important when your laptop **won't wake up**. Furthermore, HD decryption takes a long time and not guarantee to recover totally. That's why I have the chance to write this construction note : p
Here is my step to install FW tool on **Win 10**!

<img src="{filename}/res/Windows-10-Windows-7-gaming-versus-640x339.jpg" alt="Windos 10" style="width: 320px;"/>

----------


Installation
-------------

#### <i class="icon-file"></i> Backup data
- robocopy \$SRC \$DST /mir /R:0 /W:0 /FFT /A-:SH

#### <i class="icon-file"></i> Required software
- APP: Dynamic theme
- Exceed onDemand Client
- Evernote
- Notepad++
*   [Bash on Ubuntu(WSL)][1], [gcc compiler][2], [Issue: apt-get --fix-missing][3]
    * [Ubuntu file system root][7]
    * gcc, python, python3, perl, rsync
    * [bash: Bad Substitution][4], [ssh: Resource temporarily unavailable][5], [usr local bin][6]
    * apt-get install bc, libspreadsheet-parseexcel-perl

> <i class="icon-attention"></i>Check out [<i class="icon-block"></i> Firewall blocks updates to the Windows 10 Linux sub-system feature](https://support.symantec.com/en_US/article.TECH236946.html) when you see the error *ssh: connect to host tiger.synaptics.com port 22: Resource temporarily unavailable*. There is one workaround to disable firewall via **`$MYPROGRAMFILE/Symantec Endpoint Protection/Smc.exe -disable -ntp`**

- Windows Git
- Beyond compare
- Visual studio 2013/2012
- Matlab 2016/2015
- VS code
- Git extension
- P4merge
- Docker
- Git Extension
- TortoiseGit
- ZEROPLUS
- DediProg

#### <i class="icon-file"></i> Set up ssh key
- If you have one, just copy it from your old .ssh
- [How to set up ssh key](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2) 
- [Managing multiple keys](https://wiki.archlinux.org/index.php/SSH_keys)

<img src="{filename}/res/1000px-Public_key_encryption.svg.png" alt="ssh key" style="width: 320px;"/>

  [1]: https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/  
  [2]: http://www.developerinsider.in/compile-c-program-with-gcc-compiler-on-bash-on-ubuntu-on-windows-10/ "compiler gcc"
  [3]: https://askubuntu.com/questions/462690/what-does-apt-get-fix-missing-do-and-when-is-it-useful/462751 "apt-get --fix-missing"
  [4]: https://stackoverflow.com/questions/20615217/bash-bad-substitution
  [5]: https://superuser.com/questions/1098526/windows-10-linux-subsystem-ssh-client-resource-temporarily-unavailable
  [6]: https://stackoverflow.com/questions/20054538/add-a-bash-script-to-path
  [7]: https://askubuntu.com/questions/759880/where-is-the-ubuntu-file-system-root-directory-in-windows-nt-subsystem-and-vice
  [8]: http://adrai.github.io/flowchart.js/
