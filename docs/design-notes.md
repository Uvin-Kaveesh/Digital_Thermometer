# Design notes

## Signal path

The LM35 nominal transfer is 10 mV per °C, giving 0 to 990 mV across the intended 0–99 °C range. The ICL7107 uses dual-slope conversion and drives LED segments directly. The submitted design uses two visible digits, an adjustable reference, and an input divider described in the report.

## PCB considerations

The report describes a through-hole LM35, DIP-40 ICL7107, 0805 passives, aligned displays, a short sensor trace, local decoupling, and a star point for analog returns. The extracted layout and 3D views show the proposed placement. These are design intentions shown in the report, not a verified fabrication package.

## Power and calibration

The assignment calls for +5 V and −5 V at the converter. Confirm rail polarity and voltage with the ICL7107 removed before powering an assembled board. Set and measure the reference, then test several known sensor voltages. The report's formula and screenshot readings are not sufficient to establish the final calibration on their own; see [verification status](verification.md).

## Source material

- [Submitted group report](IE2044_Assignment_Group_08.pdf)
- Course assignment brief: `Assingment - PCB Design.pdf` (provided separately; not redistributed here)
- PCB workshop brief: `Workshop - PCB Desing.pdf` (provided separately; not part of this thermometer's design files)

For component specifications and circuit limits, consult the manufacturer's LM35 and ICL7107 datasheets before revising the design.
