![newlogo](./report/logo.png)
# BoneScan
## A vulnerability scanner for the BeagleBoard

### What is BoneScan?
Bone scan is a vulnerability scanner that offers users a detailed information on the security of their BeagleBoard in an easy to read report format. BoneScan is intended to be run from an administrative device separate from the BeagleBoard. The administrative device communicates with the Beagle Board via SSH.

### How do I use BoneScan?
1. Connect your BeagleBoard to the same subnet as your administrative device.
2. On the administrative device, run BoneScan.py as shown below.
`python BoneScan.py -i {ip address of BeagleBoard} -u {username of BeagleBoard}`
3. The scan may take a while. Once it is complete, the report will be saved as an html
 file in the report directory.
