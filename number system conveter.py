def convert_base(number_str, from_base, to_base):
    # Step 1: Convert input string to decimal (Base 10)
    # int() handles bases 2 through 36 automatically
    try:
        decimal_number = int(number_str, from_base)
    except ValueError:
        return "Invalid number for the given input base."

    if to_base == 10:
        return str(decimal_number)

    # Step 2: Convert decimal to the target base
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal_number == 0:
        return "0"
    
    result = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base
        result = digits[remainder] + result
        decimal_number //= to_base
        
    return result

# --- User Input ---
num = input("Enter the number: ")
base_in = int(input("Enter the current base (e.g., 2, 10, 16): "))
base_out = int(input("Enter the base to convert to: "))

output = convert_base(num, base_in, base_out)
print(f"Result: {output}")
