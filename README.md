# pyMonarc
pyMonarc is a connector application which allows python to extract the information from Monarc and, at a later stage, also save information to MONARC.

## Install and run
put all the files in one folder and copy the `loginInfo.def.cfg` to `loginInfo.cfg`. Then change the `URL` to point to your MONARC instance and fill out the authentication detail `username` and `password`.

Finally simply run `python connecter.py` and it will do its magic.

## DISCLAIMER
Keep in mind that this is a pre alpha and that currently not all information is extracted nor any information can be written! Use at your own risk: we are not liable for any problems.
