import numpy as np
from typing import Dict, List, SupportsFloat, SupportsInt, Tuple, Optional, Any


def get_deg2meter_conversion_factor(lat_deg: float) -> Tuple[float, float]:
    """
    get conversion factor between lat/long and meters
    """
    equatorial_radius = 6378137.0
    polar_radius = 6356752.314245

    lon_factor = polar_radius * np.pi / 180
    lat_factor = equatorial_radius * (np.pi / 180) * np.cos(np.deg2rad(lat_deg))

    return lon_factor, lat_factor

