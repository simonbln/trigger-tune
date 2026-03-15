# trigger-tune
Open-source audio player triggered by light beams


## Components
- RP2040 (Zero)
- DFPlayer Mini
- USB Connector
- WS2812 (NeoPixel LED)
- Audio Jack
- Micro SD Card
- Perfboard (5x7cm)
- Connectors / Cables
- Enclosure / Box
- Lightbeam normally open NPN (if other is available, you have to adjust the code. Create a Issue if you have problems here)

## Wiring Diagram
![Wiring Diagram](docu/wiring_bb.jpg)
Figure 1: Wiring diagram on the perfboard

- Connector J1 connects to the light barrier; the wiring will be split later into transmitter and receiver units. Additional light barriers can be wired in parallel here.
- Connector J2 connects to the external WS2812 LED.
- Connector J3 connects to the audio jack.

## How-To

### Breadboard Prototyping
For initial testing, it is recommended to build the circuit on a breadboard first as seen on the wiring diagram.

### Firmware Setup
1. Install **Thonny** IDE on your computer.
2. Flash the **MicroPython firmware** to the RP2040.  
   > **Firmware download:** [MicroPython for RP2040](https://micropython.org/download/rp2-pico/)
3. Copy all files from the `firmware` folder to the RP2040.

### Important: USB Power Handling
- **Do not** connect an external USB power source to the additional USB port while the RP2040 is connected to your computer via USB.
- Once the RP2040 is disconnected from the computer, the external USB port can be used to power all components. But for testing purpose you can use the USB Port of the RP2040.
- The external USB port will later be integrated into the enclosure.

### Build prototype
Solder the components and wires onto the perfboard as shown in Figure 1. Once the assembly is complete, perform an initial functional test before mounting the board into the enclosure.

![Soldering](docu/1.jpg)
![First Test](docu/2.jpg)

I decided to mount the circuit board to the lid. Since the enclosure is designed to be screwed down from the bottom, this prevents the mounting screws from interfering with the electronics. However, the board can also be mounted inside the box itself if preferred. I used rubber washers to dampen expected vibrations and minimize their transfer to the PCB.

![PCB in the lid](docu/3.jpg)

Drill the necessary holes for the cable glands and connectors, then insert them and secure with hot glue if necessary. The status LED was also routed through the lid for better visibility.


![in the enclosure 1](docu/4.jpg)
![in the enclosure 2](docu/5.jpg)
![PCB in the lid](docu/finished.jpg)

## Support me
If you find this project helpful and would like to support my work, I would be very grateful for a contribution via GitHub Sponsors or in Bitcoin (BTC) / Litecoin (LTC). Every bit of support helps me to keep creating and sharing new projects. Thank you!

LTC:
![LTC QR Code](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=DEINE_LTC_ADRESSE)
BTC:

## Third-Party Code and License

This project contains modified code from the [penguintutor/dfplayermini-pico](https://github.com/penguintutor/dfplayermini-pico) repository.

*   **Original Author:** [@PenguinTutor](https://www.penguintutor.com)
*   **Original Repository License:** **GNU General Public License v3.0** (GPL-3.0) – see full text in the original repository's `LICENSE` file.
*   **Modifications by:** ([@simonbln](https://github.com/simonbln))
*   **Date of modifications:** March 2026
*   **Nature of modifications:**
    1.  Updated `command.to_bytes(1)` to `command.to_bytes(1, 'big')` for compatibility with newer Python versions.
    2.  Fixed the return value parsing for the reset command to correctly handle the module's response.

This modified version is distributed under the same license terms (GPL-3.0). The complete license text is included in this repository as `LICENSE`.