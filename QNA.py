from PIL import Image
from pyzbar.pyzbar import decode


_removal_list = ['Rect(left=', 'top=', 'width=', 'height=', ')']
_image_path = 'C:\\Users\\Багаудин\\Desktop\\Actions\\QR\\img\\test\\ghjdt.png'


def qr_load(arg_image_path):
    decoded_qr = {}
    img_bars = decode(Image.open(arg_image_path))
    for bar in img_bars:
        decoded_qr[bar.data] = bar.rect
    return decoded_qr


def qr_iterable(def_load):
    new_qr = {}
    for key, value in def_load.items():
        new_values = (str(value))
        for word in _removal_list:
            new_values = new_values.replace(word, '')
        x = new_values.split(', ')
        zzz = integer_list(x)
        new_qr[key] = integer_list(zzz)
    return new_qr


def pythagoras(x_list):
    pif = (x_list[0]**2 + x_list[1]**2)
    return pif


def integer_list(arg_list):
    return [int(i) for i in arg_list]


def output_qr(arg_qr_iterable):
    first_load = -1
    output_data = ''
    for key, values in arg_qr_iterable.items():
        x = pythagoras(values)
        if first_load > x or first_load == -1:
            first_load = x
            output_data = key
    return output_data


def main():
    qr_load(_image_path)
    x = qr_load(_image_path)
    qr_iterable(x)
    ppp = qr_iterable(x)
    return output_qr(ppp)


print(main())
