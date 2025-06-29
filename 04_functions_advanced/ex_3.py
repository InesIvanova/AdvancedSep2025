def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""

    for cheese_name, pieces in sorted_data:
        result += f"{cheese_name}\n"
        for piece in sorted(pieces, reverse=True):
            result += f"{piece}\n"
    return result

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

