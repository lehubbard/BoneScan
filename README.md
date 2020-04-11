![logo](./report/logo.png)
# BoneScan
## A vulnerability scanner for the BeagleBoard

### What is BoneScan?
BoneScan is a vulnerability scanner that offers users detailed information on the security of their BeagleBoard in an easy to read format. BoneScan is intended to be run from an administrative device separate from the BeagleBoard. The administrative device communicates with the Beagle Board via SSH. This beta version of the scanner informs the user of potential security vulnerabilities based on recommendations by the BeagleBoard company. As an optional feature, BoneScan can check for vulnerabilities related to software installed on the BeagleBoard. [Click here for more information on securing your BeagleBoard.](https://beagleboard.org/ai/aws).

### Installation
* BoneScan requires python 3.6

* `git clone https://github.com/melvinofida/BoneScan.git`

* `pip install -e .`
### How do I use BoneScan?
* Connect your BeagleBoard to the same subnet as your administrative device.
* On the administrative device, run BoneScan.py as shown below.

* `python BoneScan/BoneScan.py`
* After the scan is completed, the results will be stored in `./report.{filename}.html`
* the --cve modifier can be used to scan for vulnerabilities related to installed software.
