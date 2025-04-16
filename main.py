#CIS-117 Lab4
#The function countriesInRegion takes the input_file of country_full.csv and first opens and reads the file, then splits it up based on the countries name and region. Then the code outputs the region files as csv files with the regions names attached.
#Tai Vutam 
#No partner

import csv


def countriesInRegion(input_file):
    try:
        with open(input_file, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            regions = {}

            for row in reader:
                try:
                    name = row['name']
                    region = row['region']
                    subregion = row['sub-region']
                except KeyError as e:
                    print(f"Missing expected column: {e}")
                    continue

                if region not in regions:
                    regions[region] = []
                regions[region].append({
                    'name': name,
                    'region': region,
                    'sub-region': subregion
                })

        for region, names in regions.items():
            filename = f"{region}.csv".replace("/", "-")
            try:
                with open(filename, mode='w', newline='') as region_file:
                    writer = csv.DictWriter(region_file, fieldnames=['name', 'region', 'sub-region'])
                    writer.writeheader()
                    writer.writerows(names)
                print(f"Created file: {filename}")
            except PermissionError:
                print(f"No permission: Unable to write to file {filename}")
            except IOError as e:
                print(f"I/O error({e.errno}): {e.strerror} when writing {filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' wasn't found.")
    except PermissionError:
        print(f"Error: No permission for file '{input_file}'.")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")
    except Exception as e:
        print(f"An error occurred: {e}")

countriesInRegion("country_full.csv")
