# DCP converter batch shell.

## About files

    - dcpTool: someone built this, can use directly, `./dcpTool -h` for helps.
    - dcp.py: written by me, auto extract dcp to xml, modify camera model, compile back to dcp, `python3 dcp.py -h` for helps.

## How to use

make sure you're in macOS.
copy some dcp files here.

open this path in terminal, then run shell

```shell
for i in ls *.dcp; do python3 dcp.py -model <XXCameraModel> -i $i; done;
```

the model name `<XXCameraModel>` change to your camera model, such as `Panasonic\ DMC-G7`, space should be prefixed `\`.