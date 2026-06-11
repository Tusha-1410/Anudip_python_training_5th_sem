# --------------------------------------------------
# Smart City Waste Collection Management System
# --------------------------------------------------

# Dictionary storing waste collected from sectors (in kg)

waste_data = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

# --------------------------------------------------
# Task 1 : Display Sectors Generating More Than 400 kg
# --------------------------------------------------

print("Sectors Generating More Than 400 kg Waste:")

for sector in waste_data:

    if waste_data[sector] > 400:

        print(sector)

# --------------------------------------------------
# Task 2 : Find Sector Generating Maximum Waste
# --------------------------------------------------

max_sector = list(waste_data.keys())[0]

for sector in waste_data:

    if waste_data[sector] > waste_data[max_sector]:

        max_sector = sector

print("\nMaximum Waste Generation:",
      max_sector,
      "(" + str(waste_data[max_sector]) + " kg)")

# --------------------------------------------------
# Task 3 : Find Sector Generating Minimum Waste
# --------------------------------------------------

min_sector = list(waste_data.keys())[0]

for sector in waste_data:

    if waste_data[sector] < waste_data[min_sector]:

        min_sector = sector

print("Minimum Waste Generation:",
      min_sector,
      "(" + str(waste_data[min_sector]) + " kg)")

# --------------------------------------------------
# Task 4 : Calculate Total Waste Collected
# --------------------------------------------------

total_waste = 0

for sector in waste_data:

    total_waste += waste_data[sector]

print("\nTotal Waste Collected:",
      total_waste,
      "kg")

# --------------------------------------------------
# Task 5 : Categorize Sectors
# --------------------------------------------------

low_waste = []
medium_waste = []
high_waste = []

for sector in waste_data:

    waste = waste_data[sector]

    if waste < 200:

        low_waste.append(sector)

    elif waste <= 400:

        medium_waste.append(sector)

    else:

        high_waste.append(sector)

print("\nLow Waste:", low_waste)
print("Medium Waste:", medium_waste)
print("High Waste:", high_waste)

# --------------------------------------------------
# Task 6 : Count Sectors Requiring Awareness Campaign
# Waste > 300 kg
# --------------------------------------------------

campaign_count = 0

campaign_sectors = []

for sector in waste_data:

    if waste_data[sector] > 300:

        campaign_count += 1

        campaign_sectors.append(sector)

print("\nSectors Requiring Awareness Campaign:")

for sector in campaign_sectors:

    print(sector)

print("\nTotal Sectors Requiring Campaign:",
      campaign_count)

# --------------------------------------------------
# Task 7 : Save Campaign Sector List to File
# --------------------------------------------------

file = open("campaign_sectors.txt", "w")

for sector in campaign_sectors:

    file.write(sector + "\n")

file.close()

print("\nCampaign Report Generated Successfully.")
