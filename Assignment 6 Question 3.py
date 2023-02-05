import json
dict = {
    "Andhra Pradesh": "Vizag",
    "Telangana": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Bihar": "Patna",
    "Odisha": "Bhubaneshwar",
    "Goa": "Panaji",
    "Tamil Nadu": "Chennai"
}
with open("State_Capitals.json","w") as f:
    json.dump(dict,f)
    