Generating QRs using python. 

All you need is an IDE(pycharm)  
pip install qrcode    
and paste the code in [qr.py](https://github.com/larymak/Python-project-Scripts/blob/main/QrCodeGen/qr.py)

This with this code you can be able to generate QR code for urls,
example:
```python
code = qrcode.make("paste url here")
```

You can also input your own message and it will still be generated:
example:
```python
image = qrcode.make(input("Write Your message: "))
```

The qrcode generated will look like below:

![image](https://github.com/larymak/Python-project-Scripts/blob/main/QrCodeGen/clock.jpg)  

Video Link: https://www.youtube.com/watch?v=QemlQBeIxWI 
[![QR Code Gen Using Python](http://i3.ytimg.com/vi/QemlQBeIxWI/maxresdefault.jpg)](https://www.youtube.com/watch?v=QemlQBeIxWI) 

