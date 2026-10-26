def format_followrs(num):
    if num >= 1000000:
        return f"{num / 1000000:.1f}M"
    elif num >= 1000:
        return f"{num / 1000:.1f}K"
    else:
        return str(num)

print(format_followrs(950))
print(format_followrs(1500))
print(format_followrs(1200000))

