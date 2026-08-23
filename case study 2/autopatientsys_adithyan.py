patient_name = input("Enter patient name: ")

requested_depts = input("Enter requested departments: ").split()
available_depts = input("Enter available departments: ").split()
visited_depts = input("Enter previously visited departments: ").split()
preferred_doctors = input("Enter preferred doctors: ").split()
available_doctors = input("Enter available doctors: ").split()
emergency_depts = input("Enter emergency departments: ").split()

print("\nPATIENT:", patient_name)

print("\nRequested departments:", requested_depts)
print("First department:", requested_depts[0])
print("First 2 departments:", requested_depts[:2])

requested_set = set(requested_depts)
available_set = set(available_depts)
visited_set = set(visited_depts)
emergency_set = set(emergency_depts)

matching_departments = requested_set & available_set

missing_departments = requested_set - available_set

visited_again = requested_set & visited_set

emergency_matches = requested_set & emergency_set

duplicate_count = len(requested_depts) - len(requested_set)

all_departments = requested_set | available_set

available_set.add("Emergency")

if "Emergency" in available_set:
    available_set.remove("Emergency")

doctor_matches = set(preferred_doctors) & set(available_doctors)

if "Cardiology" in requested_set:
    print("Cardiology is requested")

if emergency_matches:
    suggested_department = list(emergency_matches)[0]
elif matching_departments:
    suggested_department = list(matching_departments)[0]
else:
    suggested_department = "No department"

if emergency_matches:
    appointment_status = "Emergency Appointment"
elif matching_departments:
    appointment_status = "Appointment Available"
else:
    appointment_status = "Appointment Not Available"

print("\n..... APPOINTMENT REPORT .....")
print("Patient Name:", patient_name)
print("Requested:", requested_depts)
print("Available:", list(matching_departments))
print("Unavailable:", list(missing_departments))
print("Previous:", list(visited_again))
print("Emergency:", list(emergency_matches))
print("Duplicate Requests:", duplicate_count)
print("Common Doctors:", list(doctor_matches))
print("Recommended Department:", suggested_department)
print("Status:", appointment_status)