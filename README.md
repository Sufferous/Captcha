## Simple captcha generator written in python
------
### How to use:
You can either modify the code or import the `captcha.py` directly into your project.
------
### Example usage:
Generate a captcha with 7 characters:
```python
import captcha

size = 7

captcha.generate_captcha(size)
```
##### This will create a `captcha.png` file (which is the captcha) and will return the code! (The code length is determined by the size argument (default value: 6))
------
### Results:
![Captcha with code: NSBWI6](https://github.com/TheMaligator/Captcha/blob/main/captcha.png?raw=true "NSBWI6")
------
### Final thoughts:
This captcha generator isn't secure enough to use in production environments, so please, for the love of god, don't try.
It was created in order to experiment with image manipulation in python.
