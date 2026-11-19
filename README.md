<div align="center">

# LM35 + ICL7107 Digital Thermometer

**An analog temperature display, from sensor signal to PCB layout.**

`LM35` · `ICL7107` · `Proteus` · `EasyEDA Pro` · `PCB Design`

![3D view of the thermometer PCB](docs/images/pcb-design-4.png)

*EasyEDA Pro 3D preview from the submitted design report*

</div>

An analog, two-digit temperature display designed for the IE2044 Systems Modelling and Prototyping assignment at SLIIT. An LM35 produces a voltage proportional to temperature; an ICL7107 converts the signal and drives two seven-segment displays. The work includes Proteus simulation, an EasyEDA Pro PCB layout, and a breadboard prototype.

## At a glance

![Project snapshot: 0–99 °C range, LM35 sensor, ICL7107 driver, and dual supply](docs/images/project-snapshot.svg)

The design uses an LM35 sensor, an ICL7107 in a DIP-40 package, and two seven-segment digits.

## How it works

![Animated conceptual signal flow from temperature through the LM35 and ICL7107 to a two-digit display](docs/images/signal-flow.gif)

*Conceptual animation showing ideal values. It is not footage of a measured prototype.*

`Temperature → LM35 → input scaling → ICL7107 → seven-segment display`

The LM35 nominally produces `Vout = temperature (°C) × 10 mV`. For example, 25 °C corresponds to 250 mV. The ICL7107 reference and input scaling must be calibrated together so the displayed number corresponds to degrees Celsius. The assignment specifies a 100 mV reference; the submitted report also describes a 10:1 input divider. **Do not assume that setting the reference alone makes the display accurate.** Verify the actual transfer function and component values against the ICL7107 datasheet and measured circuit before fabrication or relying on a reading.

## From simulation to prototype

### 01 · Simulate the circuit

The Proteus model connects the sensor, input scaling, reference network, converter, and display.

![Proteus circuit simulation](docs/images/simulation-2.png)

### 02 · Route the board

The EasyEDA Pro layout places the DIP-40 converter between the analog circuitry and aligned display footprints.

![EasyEDA PCB routing](docs/images/pcb-design-1.png)

### 03 · Explore the assembled view

The 3D preview shows the intended component placement and two-digit front panel.

![EasyEDA PCB 3D preview](docs/images/pcb-design-3.jpg)

### 04 · Build a breadboard prototype

The submitted report includes a photo of the physical test setup.

![Breadboard prototype](docs/images/prototype-1.jpg)

## Explore the project

- **[Final report](docs/IE2044_Assignment_Group_08.pdf)** — design method, calculations, simulation, PCB views, and discussion.
- **[Design notes](docs/design-notes.md)** — signal path, layout considerations, power, and calibration.
- **[Verification status](docs/verification.md)** — what the supplied evidence shows and what still needs measurement.
- **[EasyEDA schematic](docs/images/simulation-results-1.png)** — schematic screenshot extracted from the report.

The images in this repository were extracted from the submitted report.

## Reproducing the design

1. Review the [report](docs/IE2044_Assignment_Group_08.pdf), screenshots, and the LM35 and ICL7107 datasheets.
2. Recreate the schematic in Proteus or another circuit tool. Check the ICL7107 display type, oscillator, integrator, auto-zero circuit, reference, and input scaling against the datasheet.
3. Simulate test inputs corresponding to 0, 10, 25, 50, 75, and 99 °C. Record the **actual** displayed values and reference voltage.
4. Recreate or revise the PCB in EasyEDA Pro. Check footprints, clearances, power routing, decoupling, and analog return paths before ordering.
5. Before inserting the ICL7107, measure both supply rails. Then calibrate and test the assembled circuit with a known temperature reference.

Native Proteus and EasyEDA project files were not available among the supplied materials, so the screenshots cannot be edited as source designs or used to generate manufacturing files. Gerbers and a bill of materials are likewise not included. The repository is a documented project record and starting point for recreating the design.

## Contributors

- K. G. U. K. Iranthaka — IT24103475
- P. K. S. Sanilka — IT24103564

Group 08, IE2044, 2026. Contributions are listed as in the submitted report; individual responsibilities were not documented.

## Project status

Simulation, PCB layout, and a breadboard photo are documented in the report. Quantitative hardware accuracy, a fabricated PCB, and a repeatable measured test log are not documented in the supplied files. See [verification status](docs/verification.md).
