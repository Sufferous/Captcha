## This is a simple captcha generator created in python
------
### How to use:
You can either modify the code or import the `captcha.py` directly into your project.

(Note: the captcha.py file must be in the same directory!)
------
### Example usage:
Generate a captcha with 6 characters:
```python
import captcha

size = 7

captcha.generate_captcha(size)
```
This will create a `captcha.png` file (which is the captcha) and will return the code!
(The code length is determined by the size argument (default value: 6))
------
### Results:
![Captcha with code: NSBWI6](https://github.com/TheMaligator/Captcha/blob/main/captcha.png?raw=true "NSBWI6")
------
### Final thoughts:
This captcha generator probably isn't secure enough to use in production environments, so please don't try.
Also, feel free to use this code and modify it in any way, and don't feel obligated to credit me, although it would be nice :)
