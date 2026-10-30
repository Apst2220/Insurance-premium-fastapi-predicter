tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]
tier_3_cities = [
    # Andhra Pradesh
    "Nellore", "Kurnool", "Kadapa", "Anantapur", "Eluru",
    "Ongole", "Srikakulam", "Vizianagaram", "Machilipatnam",

    # Arunachal Pradesh
    "Itanagar", "Naharlagun", "Pasighat", "Tawang",

    # Assam
    "Dibrugarh", "Silchar", "Jorhat", "Tezpur", "Tinsukia",
    "Nagaon", "Bongaigaon", "Dhubri",

    # Bihar
    "Muzaffarpur", "Bhagalpur", "Darbhanga", "Purnia",
    "Arrah", "Begusarai", "Katihar", "Munger", "Saharsa",
    "Chhapra", "Hajipur", "Bettiah", "Motihari",

    # Chhattisgarh
    "Korba", "Durg", "Rajnandgaon", "Jagdalpur", "Ambikapur",
    "Raigarh", "Dhamtari",

    # Goa
    "Margao", "Vasco Da Gama", "Mapusa", "Ponda",

    # Gujarat
    "Anand", "Nadiad", "Morbi", "Mehsana", "Palanpur",
    "Vapi", "Valsad", "Gandhidham", "Godhra", "Porbandar",
    "Junagadh", "Veraval", "Amreli", "Botad",

    # Haryana
    "Karnal", "Panipat", "Hisar", "Rohtak", "Ambala",
    "Sonipat", "Yamunanagar", "Kurukshetra", "Rewari",
    "Sirsa", "Bhiwani", "Fatehabad", "Palwal", "Kaithal",

    # Himachal Pradesh
    "Shimla", "Dharamshala", "Solan", "Mandi", "Kullu",
    "Hamirpur", "Una", "Bilaspur", "Chamba",

    # Jharkhand
    "Hazaribagh", "Deoghar", "Giridih", "Bokaro",
    "Jamshedpur", "Chaibasa", "Ramgarh", "Dumka",

    # Karnataka
    "Davangere", "Ballari", "Shivamogga", "Tumakuru",
    "Hassan", "Udupi", "Bidar", "Raichur", "Koppal",
    "Gadag", "Chitradurga", "Chikkamagaluru",
    "Bagalkot", "Vijayapura", "Yadgir", "Mandya",
    "Chamarajanagar", "Karwar", "Hospet",

    # Kerala
    "Kannur", "Thrissur", "Palakkad", "Malappuram",
    "Kollam", "Alappuzha", "Kottayam", "Kannur",
    "Kasaragod", "Pathanamthitta", "Idukki", "Wayanad",

    # Madhya Pradesh
    "Ujjain", "Sagar", "Satna", "Rewa", "Ratlam",
    "Dewas", "Burhanpur", "Khandwa", "Chhindwara",
    "Shivpuri", "Vidisha", "Betul", "Mandsaur",
    "Neemuch", "Sehore", "Itarsi",

    # Maharashtra
    "Sangli", "Satara", "Akola", "Latur", "Dhule",
    "Jalgaon", "Parbhani", "Nanded", "Osmanabad",
    "Beed", "Wardha", "Yavatmal", "Gondia", "Bhandara",
    "Chandrapur", "Ratnagiri", "Sindhudurg", "Ichalkaranji",
    "Baramati", "Panvel", "Vasai-Virar",

    # Manipur
    "Imphal", "Thoubal", "Bishnupur", "Churachandpur",

    # Meghalaya
    "Shillong", "Tura", "Jowai", "Nongstoin",

    # Mizoram
    "Aizawl", "Lunglei", "Champhai", "Serchhip",

    # Nagaland
    "Dimapur", "Kohima", "Mokokchung", "Tuensang",

    # Odisha
    "Cuttack", "Rourkela", "Sambalpur", "Puri",
    "Balasore", "Baripada", "Bhadrak", "Jharsuguda",
    "Kendujhar", "Angul", "Jeypore", "Rayagada",

    # Punjab
    "Bathinda", "Hoshiarpur", "Moga", "Pathankot",
    "Kapurthala", "Firozpur", "Faridkot", "Sangrur",
    "Barnala", "Fazilka", "Muktsar", "Gurdaspur",

    # Rajasthan
    "Kota", "Bikaner", "Ajmer", "Alwar", "Bhilwara",
    "Sikar", "Sri Ganganagar", "Chittorgarh", "Barmer",
    "Jaisalmer", "Bundi", "Tonk", "Pali", "Nagaur",
    "Banswara", "Dungarpur",

    # Sikkim
    "Gangtok", "Namchi", "Gyalshing", "Mangan",

    # Tamil Nadu
    "Erode", "Tiruppur", "Vellore", "Thoothukudi",
    "Dindigul", "Thanjavur", "Hosur", "Karur",
    "Kanchipuram", "Cuddalore", "Nagapattinam",
    "Tiruvannamalai", "Sivakasi", "Nagercoil",
    "Ramanathapuram", "Virudhunagar", "Pollachi",
    "Krishnagiri", "Ariyalur", "Perambalur",

    # Telangana
    "Karimnagar", "Khammam", "Nizamabad", "Mahbubnagar",
    "Nalgonda", "Adilabad", "Siddipet", "Suryapet",
    "Mancherial", "Ramagundam", "Jagtial",

    # Tripura
    "Agartala", "Udaipur", "Dharmanagar", "Kailashahar",

    # Uttar Pradesh
    "Gorakhpur", "Meerut", "Bareilly", "Moradabad",
    "Saharanpur", "Mathura", "Firozabad", "Jhansi",
    "Rampur", "Shahjahanpur", "Etawah", "Farrukhabad",
    "Mainpuri", "Bijnor", "Bulandshahr", "Hapur",
    "Sambhal", "Amroha", "Sitapur", "Lakhimpur",
    "Banda", "Gonda", "Faizabad", "Azamgarh",
    "Mirzapur", "Jaunpur", "Basti", "Deoria",
    "Ballia", "Unnao", "Rae Bareli", "Hardoi",

    # Uttarakhand
    "Haridwar", "Roorkee", "Haldwani", "Rudrapur",
    "Kashipur", "Rishikesh", "Pithoragarh", "Almora",

    # West Bengal
    "Howrah", "Durgapur", "Bardhaman", "Kharagpur",
    "Haldia", "Krishnanagar", "Berhampore", "Malda",
    "Raiganj", "Cooch Behar", "Bankura", "Purulia",
    "Jalpaiguri", "Darjeeling", "Kalimpong",

    # Jammu and Kashmir
    "Jammu", "Srinagar", "Anantnag", "Baramulla",
    "Udhampur", "Kathua", "Sopore",

    # Ladakh
    "Leh", "Kargil",

    # Andaman and Nicobar Islands
    "Port Blair",

    # Puducherry
    "Puducherry", "Karaikal",

    # Dadra and Nagar Haveli and Daman and Diu
    "Daman", "Silvassa",

    # Lakshadweep
    "Kavaratti"
]