
def gravitational_attraction(m1, m2, r):
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    return G * m1 * m2 / r**2
def suvat(target:str,
        
          s:float|None = None, 
          u:float|None = None, 
          v:float|None = None, 
          a:float|None = None, 
          t:float|None = None):  
    """
    Calculate missing value using SUVAT equations in kinematics.

        This function uses the standard SUVAT equations to calculate a missing kinematic value given other values.
        SUVAT stands for:
            s = displacement (m)
            u = initial velocity (m/s)
            v = final velocity (m/s)
            a = acceleration (m/s^2)
            t = time (s)

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

        Notes
        -----
        - Exactly one parameter besides target must be None for the function to work
        - All provided values must be numeric
        - Returns None and prints error message if inputs are invalid
        - Uses standard SUVAT equations from kinematics

        Examples
        --------
        >>> suvat('v', s=100, u=0, a=2, t=10)  # Calculate final velocity
        returns 20.0
    Function will return None if the inputs are invalid or insufficient
    """
    all_equations = {
        "s":{"u":"v*t-0.5*a*t**2",
              "v":"u*t+0.5*a*t**2",
              "a":"(v-u)/t",
              "t":"(v-u)/a"},
        "u":{"s":"v*t-0.5*a*t**2",
              "v":"s+0.5*a*t**2",
              "a":"(v-s)/t",
              "t":"(v-s)/a"},
        "v":{"s":"u*t+0.5*a*t**2",
              "u":"s-0.5*a*t**2",
              "a":"(s-u)/t",
              "t":"(s-u)/a"},
        "a":{"s":"v*t-u*t",
              "u":"s-v*t",
              "v":"s-u*t",
              "t":"(v-u)/s"},
        "t":{"s":"v-u/a",
              "u":"s-v/a",
              "v":"s-u/a",
              "a":"(v-u)/s"}            
    }
    all_values = {
        "s":s,
        "u":u,
        "v":v,
        "a":a,
        "t":t
    }
    if target not in all_values.keys():
        print("invalid inputs, ERROR")
        return
    unneccesary_value = None
    for key, v in all_values.items():
        if key != target and v is None:
            # print(f"Missing input for {key}")
            if unneccesary_value is None:
                unneccesary_value = key
            else:
                print("Multiple inputs are missing")
                return
    if unneccesary_value is None:
        print("All inputs are defined")
        return all_values[target]
    if unneccesary_value is not None and unneccesary_value in all_equations[target].keys():
        target_equation = all_equations[target][unneccesary_value]
        # Convert equation string to expression using values from all_values
        local_vars = {}
        for element, v in all_values.items():
            if v is not None:
                local_vars[element] = v
        result = eval(target_equation, {"__builtins__": {}}, local_vars)
        return result
if __name__ == "__main__":
    # Example usage:
    # A car starts from a stop light, how far has it travelled when it reaches 10 m/s, accelerating at 10 m/s^2?
    print(suvat("s", u=0, v=10, a=10, t=None))


