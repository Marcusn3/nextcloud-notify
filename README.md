# nextcloud-notify


###Installation & Usage

####Install Kdeconnect, pair your device and note the Device ID:

`$ sudo apt install kdeconnect`

`$ kdeconnect-cli -l`

`Output: - devicetype(ex. moto g(6)): device-id`

`$ kdeconnect-cli -d device-id --pair`


####Enter your device ID in the code:

```python
#replace
success = "kdeconnect-cli -d ################ --ping-msg 'notification_message'"
#with
success = "kdeconnect-cli -d your_device_id --ping-msg 'notification_message'"


```
