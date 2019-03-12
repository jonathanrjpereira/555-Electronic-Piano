# Electronic Piano | LM555
An electronic piano that uses the 555 to generate eight different piano notes.

**Order PCB:**

## Electronic Components
| Qty | Component | Buy |
| ------------- | ------------- | ------------- |
| 1 | 555 |[AliExpress](http://s.click.aliexpress.com/e/sCv1ACC) |
| 1 | 390Ω, 620Ω, 910Ω, 1.1KΩ, 1.3KΩ, 1.5K, 2KΩ, 6.2KΩ |[AliExpress](http://s.click.aliexpress.com/e/bh4eqrQs) |
| 2 | 1KΩ Resistor |[AliExpress](http://s.click.aliexpress.com/e/bh4eqrQs) |
| 8 | Tactile Momentary Push Buttons |[AliExpress](http://s.click.aliexpress.com/e/c77Ajrpq) |
| 1 | 5mm LED |[AliExpress](http://s.click.aliexpress.com/e/wuFpLXS) |
| 1 | 0.1uF Capacitor |[AliExpress](http://s.click.aliexpress.com/e/c9FHzl5W) |
| 1 | 10nF Capacitor |[AliExpress](http://s.click.aliexpress.com/e/byQG0DZW) |
| 2 | 2 Pin Screw Terminal |[AliExpress](http://s.click.aliexpress.com/e/xYUweh2) |
| 1 | Speaker |[AliExpress](http://s.click.aliexpress.com/e/brMJh46c) |
| 1 | 9V Battery Holder |[AliExpress](http://s.click.aliexpress.com/e/c3jbp72Y) |
| 1 | 9V Battery |[AliExpress](http://s.click.aliexpress.com/e/bbDirGHE) |
| 1 | PCB |[AliExpress](http://s.click.aliexpress.com/e/dhgwzKY) |


| Tools | Buy |
|--|--|
|Soldering Iron|[AliExpress](http://s.click.aliexpress.com/e/E83bSJI) |
|Soldering Wire|[AliExpress](http://s.click.aliexpress.com/e/PdhB0nm) |
|Mini PCB Hand Drill + Bits|[AliExpress](http://s.click.aliexpress.com/e/b93tomjI) |

## Working
**LM555/NE555:**

The 555 is a highly stable device for generating accurate time delays or oscillation. Additional terminals are provided for triggering or resetting if desired. For stable operation as an oscillator, the free running frequency and duty cycle are accurate controlled with two external resistors and one capacitor. The circuit may be triggered and reset on falling waveforms, and he output circuit can source or sink up to 200mA or drive TTL circuits.

![Pinout](https://github.com/jonathanrjpereira/555-Electronic-Piano/blob/master/img/pinout.png)
![Pin Description](https://github.com/jonathanrjpereira/555-Electronic-Piano/blob/master/img/pindescription.png)


**Circuit:**

The circuit is connected such that it will trigger itself and free run as an astable multivibrator. The external capacitor charges through Ra+Rb and discharges through Rb. Thus th duty cycle may be precisely set by the ratio of these two resistors.

In this mode of operation, the capacitor charges and discharges between 1/3 VCC and 2/3 VCC. Hence the charge and discharge times, and therefore the frequency are independent of the supply voltage.

The change time (output high) is given by:
<img src="https://latex.codecogs.com/gif.latex?\inline&space;t_{1}&space;=&space;0.693&space;(R_{A}&space;&plus;&space;R_{B})C" title="t_{1} = 0.693 (R_{A} + R_{B})C" />

And the discharge time (output low) by:
<img src="https://latex.codecogs.com/png.latex?\inline&space;t_{2}&space;=&space;0.693(R_{B})C" title="t_{2} = 0.693(R_{B})C" />

Thus the total period is:
<img src="https://latex.codecogs.com/png.latex?\inline&space;T&space;=&space;t_{1}&space;&plus;&space;t_{2}&space;=&space;0.693(R_{A}&plus;2R_{B})C" title="T = t_{1} + t_{2} = 0.693(R_{A}+2R_{B})C" />

The frequency of oscillation is:
<img src="https://latex.codecogs.com/png.latex?\inline&space;f&space;=&space;\frac{1}{T}&space;=&space;\frac{1.44}{(R_{A}&plus;2R_{B})C}" title="f = \frac{1}{T} = \frac{1.44}{(R_{A}+2R_{B})C}" />

Hence
<img src="https://latex.codecogs.com/png.latex?\inline&space;R_{B}&space;=&space;\frac{1}{2}(\frac{1}{.7C&space;\times&space;f}&space;-&space;R_{A})" title="R_{B} = \frac{1}{2}(\frac{1}{.7C \times f} - R_{A})" />

![Block Diagram](https://github.com/jonathanrjpereira/555-Electronic-Piano/blob/master/img/BD.png)

An input trigger such as a switch or button is pressed which connects its corresponding resistance within the resistor chain to the IC 555 which acts as an Astable Multivibrator. Depending on the value of the resistance the speaker will produce a different sound.

![Frequency Resistor Chart](https://github.com/jonathanrjpereira/555-Electronic-Piano/blob/master/img/rchain.png)

Each piano key has a separate frequency associated with it as shown in the table below.
We have kept the values of Ra & C as constant and only vary the value of Rb in order to change the frequency whenever a different key is pressed. In order to do this we created a resistor chain according to the table above as shown in the schematic. This chain is configured to optimize and reduce the number of individual resistors required.

![Schematic](https://github.com/jonathanrjpereira/555-Electronic-Piano/blob/master/img/sch.png)



## Contributing🛠
Are you an engineer or hobbyist who has a great idea for a new feature in this project? Maybe you have a good idea for a bug fix? Feel free to grab our code & schematics from Github and tinker with it. Don't forget to smash ⭐️ & the Pull Request button.

[![alt text][1.1]][1] [![alt text][2.1]][2] [![alt text][3.1]][3]

[1.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/youtube.png (YouTube)
[2.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/instagram.png (Instagram)
[3.1]: https://github.com/jonathanrjpereira/Social-Media-README/blob/master/github.png (GitHub)

[1]: https://www.youtube.com/channel/UCRW-41O1vy98KKgJRQoYzdg
[2]: https://www.instagram.com/electroguruji/
[3]: https://github.com/jonathanrjpereira
