import math

def cartesian_to_polar(x, y):
    """
    Converts Cartesian coordinates (x, y) to polar coordinates (r, θ).
    Returns r (radius) and θ (angle in radians).
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)  # atan2 correctly determines the angle
    return r, theta

def polar_to_cartesian(r, theta):
    """
    Converts polar coordinates (r, θ) to Cartesian coordinates (x, y).
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

if __name__ == "__main__":
    # Example usage
    x, y = 3, 4
    r, theta = cartesian_to_polar(x, y)
    print(f"Cartesian: ({x}, {y}) → Polar: (r={r:.2f}, θ={math.degrees(theta):.2f}°)")

    x_new, y_new = polar_to_cartesian(r, theta)
    print(f"Back to Cartesian: ({x_new:.2f}, {y_new:.2f})")