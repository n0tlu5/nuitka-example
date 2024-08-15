# compare module
a simple python module for experimenting with nuitka

# build wrapper

place the shared object file at `wrapper/` first

```bash
python3 setup.py sdist
```

the archive file will be at `dist/`

# build module

```bash
./build.sh
```

it will produce the shared object file

