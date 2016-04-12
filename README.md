# python-powertop

A wrapper to use [PowerTOP](https://01.org/powertop/) easily in Python.

## Install

```
sudo python3 -m pip install powertop
```

## Short example

Run as root, in a Python 3 shell:

```
import powertop
import pprint

measures = powertop.Powertop().get_measures(time=1)

pprint.pprint(measures['Device Power Report'][0].rows())
```

Outputs:

```
[{'Device Name': 'CPU misc', 'Usage': '29,3%'},
 {'Device Name': 'DRAM', 'Usage': '29,3%'},
 {'Device Name': 'CPU core', 'Usage': '29,3%'},
 {'Device Name': 'GPU misc', 'Usage': '67,4 ops/s'},
 {'Device Name': 'GPU core', 'Usage': '67,4 ops/s'},
 {'Device Name': 'Display backlight', 'Usage': '26,4%'},
 ...
```

## How to use

First, call PowerTOP:

```
import powertop

measures = powertop.Powertop().get_measures(time=1, iterations=1)
```

### Sections

You can then access sections. They may vary across systems and PowerTOP versions.

On my computer, they are:

* Top 10 Power Consumers
* Processor Idle State Report
* Processor Frequency Report
* Overview of Software Power Consumers
* Device Power Report
* Process Device Activity
* Software Settings in Need of Tuning
* Untunable Software Issues
* Optimal Tuned Software Settings

You can find yours with this command:

```
sudo python3 -c "import powertop; measures = powertop.Powertop().get_measures(time=1); print(measures.keys())"
```

### Reading sections

Each section is a list of CSV-decoded arrays

Use `measure['Section Name'][i].rows()` to get the content of the `i`th table section, as a list of dicts (`header => value`).

PowerTOP's tables do not always make sense (eg. two different tables concatenated), you will have to figure out how to use them.
