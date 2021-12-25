# raw-socket-testing

```sh
sudo python3 recv.py --interface eth0
```

```sh
sudo python3 send.py \
  --interface enp9s0 \
  --to b827eb24fd38 \
  "`echo 'Hello!'` at `date -Is`"
```
