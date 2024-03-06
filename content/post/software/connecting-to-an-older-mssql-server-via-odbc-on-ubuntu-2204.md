---
date: "2024-03-06"
tags: ["mssql", "odbc"]
title: "Connecting to an older MSSQL Server via ODBC on Ubuntu 22.04"
---

Some years ago I wrote [this post](til_211129_1/) on some system settings I needed to connect to an older version of Microsoft SQL Server from Ubuntu 21.04. I'm now on Ubuntu 22.04 and had to make a few extra changes in addition to those in the previous post.

## Package Changes

The Ubuntu 22.04 MSSQL-related packages are in an APT list file and need to be added to APT sources:

```bash
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt update
```

After that packages to connect MSSQL via ODBC can be installed:

```bash
ACCEPT_EULA=Y apt install -y msodbcsql17 unixodbc unixodbc-dev
```

## OpenSSL Adjustment

On Ubuntu 21.04 an OpenSSL **SECLEVEL** of 1 was sufficient to connect to my MSSQL servers. On 22.04 I needed to set the **SECLEVEL** to 0. The changes to make to a vanilla */etc/ssl/openssl.cnf* file now become:

```ini
[ssl_sect]
system_default = system_default_sect

[system_default_sect]
MinProtocol = TLSv1.2
CipherString = DEFAULT:@SECLEVEL=0

[legacy_sect]
activate = 1

[ default_conf ]
ssl_conf = ssl_sect
```

