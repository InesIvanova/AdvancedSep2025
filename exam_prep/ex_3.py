def list_roman_emperors(*args, **kwargs):
    success_emperors = {}
    failed_emperors = {}

    for emp_name, success_status in args:
        if success_status:
            success_emperors[emp_name] = kwargs[emp_name]
        else:
            failed_emperors[emp_name] = kwargs[emp_name]

    sorted_success_emperors = sorted(success_emperors.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    sorted_failed_emperors = sorted(failed_emperors.items(), key=lambda kvp: (kvp[1], kvp[0]))

    result = f"Total number of emperors: {len(args)}"
    if success_emperors:
        result  += "\nSuccessful emperors:"
        for emp_name, years in sorted_success_emperors:
            result += f"\n****{emp_name}: {years}"
    if sorted_failed_emperors:
        result += "\nUnsuccessful emperors:"
        for emp_name, years in sorted_failed_emperors:
            result += f"\n****{emp_name}: {years}"

    return result


print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))