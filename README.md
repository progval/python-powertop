# python-powertop

A wrapper to use [PowerTOP](https://01.org/powertop/) easily in Python.

## Short example

Run as root:

```
import powertop
import pprint

measures = powertop.Powertop().get_measures(time=1)

pprint.pprint(measures['Device Power Report'].rows())
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

## Install

```
sudo python3 -m pip install powertop
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

Each sections contains decoded CSV data.

Use `measure['Section Name'].rows()` to get the content of a section, as a list of dicts (`header => value`).

PowerTOP concatenates arrays, so headers do not make sense for all sections.
