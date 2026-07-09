# PBH reusable code

Put `output_xe.dat` or `output.dat` in this folder.

## Files

```text
pbh_reusable_v2/
├── output_xe.dat or output.dat
├── figures.py             # only YAH'17 Figures 6-9
├── self_consistent.py     # Roy's radiation-pressure self-consistent luminosity work
├── expansion_check.py     # t_B H diagnostic plot
├── main.py                # runs everything
└── pbh/
    ├── __init__.py
    ├── constants.py
    ├── history.py
    ├── bondi.py
    ├── luminosity.py
    └── utils.py
```

The `pbh` package contains only the reusable baseline physics functions.
The new self-consistent luminosity work lives outside the package in `self_consistent.py`.

## Run

```bash
python figures.py
python self_consistent.py
python expansion_check.py
python main.py
```
