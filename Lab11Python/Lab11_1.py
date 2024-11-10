import csv

def process_population_data(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            population_data = {}
            min_population = float('inf')
            max_population = float('-inf')
            min_year = max_year = None
            start_year = 1991

            for row in reader:
                if row[0] == 'Population, total' and row[2] == 'Ukraine':
                    for i, value in enumerate(row[4:34]):
                        year = start_year + i
                        population = int(value)
                        population_data[year] = population

                        if population < min_population:
                            min_population = population
                            min_year = year
                        if population > max_population:
                            max_population = population
                            max_year = year

            print("Population data for Ukraine (1991-2019):")
            for year, population in population_data.items():
                print(f"{year}: {population}")

            with open(output_file, "w", newline='', encoding='utf-8') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(['Year', 'Population'])
                for year, population in population_data.items():
                    writer.writerow([year, population])
                writer.writerow(["Minimum Population Year", min_year, 'Population', min_population])
                writer.writerow(["Maximum Population Year", max_year, 'Population', max_population])

            print(f"\nResults saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError as e:
        print(f"Error: Unable to convert data to integer: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "data.csv"
    output_file = "population_analysis.csv"
    process_population_data(input_file, output_file)
