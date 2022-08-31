# CSGO PYTHON EXTERNAL WALLHACK
Simple External ESP for CS:GO.

## Get Started
1. Clone the repository
```
git clone https://github.com/Kava4/CSGO-External-Python-Wallhack.git
```

2. Install the prerequisites
```
pip install -r requirements.txt
```

3. Execute the script in a terminal with elevated privileges 
```
python csgo-wall.py
```

## Common Issues
* Issue: The token does not have the specified privilege.
    * Fix: The terminal or interpreter must be ran with administrator privileges.

* Issue: `AttributeError: 'NoneType' object has no attribute` or any other Python error.
    * Fix: Make sure you are running at least Python 3.5 (earlier versions are unsupported, future versions may have breaking issues), have installed the correct versions of the required modules from requirements.txt, and have updated the offsets to the latest version of CS:GO. Very rarely this issue can be caused by a major gane update but it's only happened twice before.

## Requirements
* Windows (minimum Vista, recommended 7/8.1/10)
* [Python 3.5](https://www.python.org/downloads/)
* [Python for Windows Extensions](https://github.com/mhammond/pywin32)
* [Pymem](https://github.com/srounet/Pymem)