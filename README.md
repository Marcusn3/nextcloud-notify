# nextcloud-notify


### Installation & Usage

  ##### Install Requirements, pair your device and note the Device ID:

`$ sudo apt install kdeconnect`

`$ pip3 install schedule`

`$ kdeconnect-cli -l`

`Output: - devicetype(ex. moto g(6)): device-id`

`$ kdeconnect-cli -d device-id --pair`


##### Enter your device ID in the code:

```python
#replace
success = "kdeconnect-cli -d ################ --ping-msg 'notification_message'"
#with
success = "kdeconnect-cli -d your_device_id --ping-msg 'notification_message'"


```
#### Usage:

run `$ nohup python3 ~/nextcloud-notify/nextcloud-notify.py &`

### Note: If you reboot your device while the script is running, you have to start the script again after rebooting
