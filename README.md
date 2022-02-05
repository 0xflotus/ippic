# ippic

ippic is a tool to create an image from an IP address.

```bash
> python3 -m ippic 127.0.0.1
```

This command will produce a `ip.png` file in your current directory. 

The image of the IPv4 localhost address will be:

![localhost ipv4](./docs/localhost_v4.png)

ippic can recognize IPv4 or IPv6 addresses, also in compressed form.

```bash
> python3 -m ippic ::1 

> python3 -m ippic 0000:0000:0000:0000:0000:0000:0000:0001
```

Both commands above will produce the following image:

![localhost ipv4](./docs/localhost_v6.png)

## Other examples

```bash
> python3 -m ippic 2a00:1450:4001:82b::2003
```

![example](./docs/example.png)