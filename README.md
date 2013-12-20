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

```bash
racadm -H 10.0.0.100 -u root -p calvin -c "getconfig -g cfgServerInfo"
```
