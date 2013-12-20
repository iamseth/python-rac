python-rac
=============

Implementation of racadm in pure Python


Installation
=============

```bash
python setup.py test
sudo python setup.py install
```

Usage
=============

### View server config information
```bash
racadm -H 10.0.0.100 -u root -p calvin -c "getconfig -g cfgServerInfo"
```

### Set first boot device to PXE just once
```bash
racadm -H 10.0.0.100 -u root -p calvin -c "getconfig -g cfgServerInfo -o cfgServerFirstBootDevice pxe"
racadm -H 10.0.0.100 -u root -p calvin -c "getconfig -g cfgServerInfo -o cfgServerBootOnce 1"
```

### Reboot the host
```bash
racadm -H 10.0.0.100 -u root -p calvin -c "serveraction powercycle"
```

