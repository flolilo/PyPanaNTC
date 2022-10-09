# LAN control protocol "Protocol2" (projector) #


## Password has been set (protected mode) ##


### Connection procedure ###

 - Connect via TCP to correct IP, port 1024 (typically)
 - Response from device is `NTCONTROL 1 xxxxxxxx\r` (`NTCONTROL0x200x310x20xxxxxxxx0x0D`); `xxxxxxxx` being a hexadecimal random code.
 - Generate an 32b MD5-hash in the scheme of: `<user>:<password>:xxxxxxxx`; where `<user>` is typically `admin1` or `dispadmin`, `<password>` is typically `panasonic`, and `xxxxxxxx` is the random code from above. This hash value will be used for sending commands.


### Sending commands ###

Commands always start with the above mentioned hash followed by `00`, then the command which can be found in your device's RS-232C--sheet, and end with `0x0d` (carriage return, `\r`):

`<32b MD5 hash from above>00<COMMAND>\r` (`<32b MD5 hash from above>0x300x30<COMMAND>0x0d`)


### Response ###

`00<ResponseData>\r` (`0x300x30<ResponseData>0x0d`)


### Error responses ###

 - `ERR1`: Undefined control command
 - `ERR2`: Parameter out of range
 - `ERR3`: Busy state or unavailable period
 - `ERR4`: Time out or unavailable period
 - `ERR5`: Invalid data length
 - `ERRA`: Mismatching state of password
 - `ER401`: Error occurred on processing command
 - `ER402`: Invalid parameter (???)


## Password has not been set (non-protected mode) ##


### Connection procedure ###

 - Connect via TCP to correct IP, port 1024 (typically)
 - Response from device is `NTCONTROL 0\r` (`NTCONTROL0x200x300x0d)
 
 
### Sending commands ###

Commands always start with `00`, then the command which can be found in your device's RS-232C--sheet, and end with `0x0d` (carriage return, `\r`):

`00<COMMAND>\r` (`0x300x30<COMMAND>0x0d`)


### Response ###

`00<ResponseData>\r` (`0x300x30<ResponseData>0x0d`)


### Error responses ###

 - `ERR1`: Undefined control command
 - `ERR2`: Parameter out of range
 - `ERR3`: Busy state or unavailable period
 - `ERR4`: Time out or unavailable period
 - `ERR5`: Invalid data length
 - `ER401`: Error occurred on processing command
 - `ER402`: Invalid parameter (???)
