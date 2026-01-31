"""
kontakt2mpce - Convert Native Instruments Kontakt instruments to Akai MPC Keygroup format.

This package provides tools to convert Kontakt .nki files to MPC .xpm files,
focusing on multi-sample mapping and playback functionality.
"""

__version__ = "0.1.0"
__author__ = "Adam Jablonski"

from kontakt2mpce.converter import convert_nki_to_xpm

__all__ = ["convert_nki_to_xpm"]
