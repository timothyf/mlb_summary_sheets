


class Utils:

    @staticmethod
    def format_stat(value, format_spec):
        """Function to apply appropriate formatting to a stat."""

        # Check if the format_spec is a function (e.g., lambda)
        if callable(format_spec):
            return format_spec(value)  # Call the function to format the value

        # Check for percent formatting
        if format_spec == 'percent':
            return f"{value * 100:.1f}%"
        
        # Custom formatting for removing leading zero before the decimal
        if isinstance(format_spec, str) and 'no_leading_zero' in format_spec:
            formatted_value = f"{value:.3f}"  # Format with three decimal places
            return formatted_value.lstrip('0')  # Remove leading zero if present
        
        # Ensure format_spec is a string before using format()
        if isinstance(format_spec, str):
            return format(value, format_spec)
        
        # If format_spec is not a string, raise an error or handle appropriately
        raise TypeError(f"Invalid format_spec: {format_spec}. Expected a string or callable.")
