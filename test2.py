# import os.path
from typing import List, Dict, Union

from astropy.coordinates import get_body
from astropy.coordinates import solar_system_ephemeris, EarthLocation, get_constellation
from astropy.time import Time
# from PIL import Image

# from pathlib import Path

ZODIAC_LIST = ['Aquarius', 'Aries', 'Cancer', 'Capricornus', 'Gemini', 'Leo', 'Libra', 'Pisces', 'Sagittarius',
               'Scorpius', 'Taurus', 'Virgo']


def call_astral(advanced_details: bool = False, reversed: bool = False) -> Union[Dict, List]:
    """
    gets all planets, moon and sun position in sky
    :param advanced_details: bool
            If true, prints all the solar system planets with evert body near them
    :return: dictionary containing a planet and its constellation position
    """

    solar_system_ephemeris.set('de432s')
    loc = EarthLocation.from_geodetic(lon=40.416729, lat=-3.703339)
    t = Time.now()

    moon_constell = get_constellation(get_body('moon', t, loc))
    mercury_constell = get_constellation(get_body('mercury', t, loc))
    venus_constell = get_constellation(get_body('venus', t, loc))
    mars_constell = get_constellation(get_body('mars', t, loc))
    jupiter_constell = get_constellation(get_body('jupiter', t, loc))
    saturn_constell = get_constellation(get_body('saturn', t, loc))
    uranus_constell = get_constellation(get_body('uranus', t, loc))
    neptune_constell = get_constellation(get_body('neptune', t, loc))
    pluto_constell = get_constellation(get_body('pluto', t, loc))
    sun_constell = get_constellation(get_body('sun', t, loc))

    constel_dict = {'sun': sun_constell, 'moon': moon_constell, 'mercury': mercury_constell, 'venus': venus_constell,
                    'mars': mars_constell, 'jupiter': jupiter_constell, 'saturn': saturn_constell,
                    'uranus': uranus_constell,
                    'neptune': neptune_constell, 'pluto': pluto_constell}

    if not reversed:
        return constel_dict

    constel_dict = {k: v if v in ZODIAC_LIST else None for (k, v) in constel_dict.items()}

    constel_dict = invert_dictionary_map(constel_dict)

    if None in constel_dict:
        constel_dict.pop(None)

    constel_dict = [
        {"Aries": constel_dict.get('Aries', [None])},
        {"Taurus": constel_dict.get('Taurus', [None])},
        {"Gemini": constel_dict.get('Gemini', [None])},
        {"Cancer": constel_dict.get('Cancer', [None])},
        {"Leo": constel_dict.get('Leo', [None])},
        {"Virgo": constel_dict.get('Virgo', [None])},
        {"Libra": constel_dict.get('Libra', [None])},
        {"Scorpio": constel_dict.get('Scorpio', [None])},
        {"Sagittarius": constel_dict.get('Sagittarius', [None])},
        {"Capricorn": constel_dict.get('Capricorn', [None])},
        {"Aquarius": constel_dict.get('Aquarius', [None])},
        {"Pisces": constel_dict.get('Pisces', [None])},
    ]

    return constel_dict


def invert_dictionary_map(my_map):
    inv_map = {}
    for k, v in my_map.items():
        inv_map[v] = inv_map.get(v, []) + [k]

    return inv_map


# def overlap_images(image1_path, image2_path):
#     """
#     Overlaps two png images
#     :param image1_path: str
#             Image 1 path
#     :param image2_path: str
#             Image 2 path
#     :return:
#     """
#     # Open the images
#     img1 = Image.open(image1_path)
#     img2 = Image.open(image2_path)
#
#     # Ensure both images have an alpha channel (transparency)
#     img1 = img1.convert("RGBA")
#     img2 = img2.convert("RGBA")
#
#     # Paste img2 onto img1 at the specified position
#     img1.paste(img2, (0, 0), img2)
#
#     # Save the result
#     return img1


# def create_constell_img(const_dict: dict, base_dir: Path):
#     """
#     Creates full constellation image
#     :param base_dir: Path
#             Path to the base dir with images
#     :param const_dict: dict
#             Constellation dictionary
#     :return:
#     """
#     base_img = Image.open(base_dir / "base.png")
#     base_img = base_img.convert("RGBA")
#
#     for k, v in const_dict.items():
#         for planet in v:
#             base_img = overlap_images(base_img, os.path.join(k, planet + ".png"))
#
#     base_img.save("static/constellation_img.png", "PNG")


if __name__ == '__main__':
    out = call_astral(True)
    # create_constell_img(out)

    print(out)
