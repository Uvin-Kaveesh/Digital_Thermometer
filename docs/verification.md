# Verification status

| Claim | Evidence available | Status |
| --- | --- | --- |
| LM35 nominal output is 10 mV/°C | Assignment brief and report | Design assumption; check datasheet and sensor |
| Temperature changes were simulated | Proteus screenshots and report | Documented visually |
| PCB layout was designed | EasyEDA screenshots in report | Documented visually |
| Physical prototype was assembled | Breadboard photo in report | Documented visually |
| Display reads 0–99 °C accurately | Expected-value table in report | **Not independently verified** |
| Fabricated PCB works | No fabricated-board evidence supplied | **Not verified** |

The report's expected-value table lists readings at 0, 10, 25, 30, 50, 75, and 99 °C, but does not provide a measured table with observed values and error. One extracted Proteus screenshot shows a displayed value that does not match the sensor setting visible in that screenshot. The report also presents a divider calculation that yields 361 for a nominal 36 °C example. These discrepancies need a fresh calibration and test record before claiming measurement accuracy.

## Suggested test record

| Reference temperature (°C) | LM35 voltage (mV) | Reference voltage (mV) | Display reading (°C) | Error (°C) |
| ---: | ---: | ---: | ---: | ---: |
| 0 | | | | |
| 10 | | | | |
| 25 | | | | |
| 50 | | | | |
| 75 | | | | |
| 99 | | | | |

Measure both rails before inserting the converter. Record the instrument and reference used for each test. Add actual readings here when available.
