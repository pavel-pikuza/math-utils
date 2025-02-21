import math

def cartesian_to_polar(x, y, is_clockwise=False):
    """
    Converts Cartesian coordinates (x, y) to polar coordinates (r, θ).
    
    Parameters:
        x (float): X coordinate.
        y (float): Y coordinate.
        is_clockwise (bool): If True, angle is measured clockwise.

    Returns:
        r (float): Radius.
        theta (float): Angle in degrees (clockwise or counterclockwise).
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.degrees(math.atan2(y, x))
    
    if is_clockwise:
        theta = -theta  # Invert the angle if measured clockwise

    return r, theta

def polar_to_cartesian(r, theta, is_clockwise=False):
    """
    Converts polar coordinates (r, θ in degrees) to Cartesian coordinates (x, y).

    Parameters:
        r (float): Radius.
        theta (float): Angle in degrees (clockwise or counterclockwise).
        is_clockwise (bool): If True, the angle is assumed to be clockwise.

    Returns:
        x (float): X coordinate.
        y (float): Y coordinate.
    """
    if is_clockwise:
        theta = -theta  # Invert the angle back if it was measured clockwise

    theta_rad = math.radians(theta)
    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)

    return x, y

def shift_coordinates(x, y, new_origin_x, new_origin_y):
    """
    Shifts the coordinate system so that (new_origin_x, new_origin_y) becomes (0,0).
    
    Parameters:
        x (float): Original x-coordinate.
        y (float): Original y-coordinate.
        new_origin_x (float): X-coordinate of the new origin.
        new_origin_y (float): Y-coordinate of the new origin.

    Returns:
        tuple: Shifted coordinates (x', y') relative to the new origin.
    """
    shifted_x = x - new_origin_x
    shifted_y = y - new_origin_y
    return shifted_x, shifted_y


if __name__ == "__main__":
    # Example usage
    x, y = 3, 4
    r, theta = cartesian_to_polar(x, y)
    print(f"Cartesian: ({x}, {y}) → Polar: (r={r:.2f}, θ={theta:.2f}°)")

    x_new, y_new = polar_to_cartesian(r, theta)
    print(f"Back to Cartesian: ({x_new:.2f}, {y_new:.2f})")