import math

def gravitational_attraction(m1, m2, r):
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    return G * m1 * m2 / r**2

def find_dist(pair_of_points):
    return math.sqrt(pair_of_points[0]**2 + pair_of_points[1]**2)

def suvat(target: str,
          s: float | None = None,
          u: float | None = None,
          v: float | None = None,
          a: float | None = None,
          t: float | None = None):
    """
    Calculate missing value using SUVAT equations in kinematics.

    Parameters
    ----------
    target : str
        The variable to solve for ('s', 'u', 'v', 'a', or 't')
    s : float, optional
        Displacement in meters
    u : float, optional
        Initial velocity in meters per second
    v : float, optional
        Final velocity in meters per second
    a : float, optional
        Acceleration in meters per second squared
    t : float, optional
        Time in seconds

    Returns
    -------
    float or None
        The calculated value for the target variable if solvable,
        None if the inputs are invalid or insufficient
    """
    # Count how many variables are None (should be exactly 1 - the target)
    none_count = sum(1 for var in [s, u, v, a, t] if var is None)
    if none_count != 1:
        print("Error: Exactly one variable (besides target) must be None")
        return None

    try:
        if target == 's':
            if t is not None and u is not None and a is not None:
                return u * t + 0.5 * a * t**2
            elif v is not None and u is not None and a is not None:
                return (v**2 - u**2) / (2 * a)
            elif v is not None and u is not None and t is not None:
                return 0.5 * (u + v) * t
            else:
                print("Insufficient information to solve for displacement (s)")
                return None

        elif target == 'u':
            if v is not None and a is not None and t is not None:
                return v - a * t
            elif s is not None and a is not None and t is not None:
                return (s - 0.5 * a * t**2) / t
            elif v is not None and s is not None and t is not None:
                return (2 * s) / t - v
            else:
                print("Insufficient information to solve for initial velocity (u)")
                return None

        elif target == 'v':
            if u is not None and a is not None and t is not None:
                return u + a * t
            elif u is not None and a is not None and s is not None:
                return math.sqrt(u**2 + 2 * a * s)
            elif s is not None and t is not None and u is not None:
                return (2 * s) / t - u
            else:
                print("Insufficient information to solve for final velocity (v)")
                return None

        elif target == 'a':
            if v is not None and u is not None and t is not None:
                return (v - u) / t
            elif s is not None and u is not None and t is not None:
                return 2 * (s - u * t) / t**2
            elif v is not None and u is not None and s is not None:
                return (v**2 - u**2) / (2 * s)
            else:
                print("Insufficient information to solve for acceleration (a)")
                return None

        elif target == 't':
            if v is not None and u is not None and a is not None:
                return (v - u) / a
            elif s is not None and u is not None and a is not None:
                # Solve quadratic equation: s = ut + ½at²
                discriminant = u**2 + 2 * a * s
                if discriminant < 0:
                    print("No real solution exists for time")
                    return None
                t1 = (-u + math.sqrt(discriminant)) / a
                t2 = (-u - math.sqrt(discriminant)) / a
                # Return the positive solution
                return max(t for t in [t1, t2] if t >= 0)
            elif s is not None and u is not None and v is not None:
                return (2 * s) / (u + v)
            else:
                print("Insufficient information to solve for time (t)")
                return None

        else:
            print("Invalid target variable")
            return None

    except TypeError:
        print("Error: All provided values must be numeric")
        return None
    except ZeroDivisionError:
        print("Error: Division by zero occurred")
        return None

if __name__ == "__main__":
    # Test cases
    print("1. Calculate displacement (s):", suvat('u', t=1, v=10, a=-9.8))  # Should return 25.0
    # print("2. Calculate initial velocity (u):", suvat('u', s=100, v=20, a=2, t=10))  # Should return 0.0
    # print("3. Calculate final velocity (v):", suvat('v', u=5, a=3, t=4))  # Should return 17.0
    # print("4. Calculate acceleration (a):", suvat('a', u=0, v=10, s=50))  # Should return 1.0
    # print("5. Calculate time (t):", suvat('t', u=0, v=10, a=2))  # Should return 5.0
