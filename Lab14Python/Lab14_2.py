import csv
import matplotlib.pyplot as plt

def read_data(file_path, indicator, country1, country2):
    data_country1 = []
    data_country2 = []
    years = [2002, 2003, 2004, 2005]

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == country1 and row[2] == indicator:
                    data_country1 = [int(row[i]) for i in range(4, 8)]
                elif row[0] == country2 and row[2] == indicator:
                    data_country2 = [int(row[i]) for i in range(4, 8)]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except ValueError as ve:
        print(f"Data conversion error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return years, data_country1, data_country2

def plot_line_chart(years, data1, data2, country1, country2, indicator):
    plt.figure(figsize=(10, 6))
    plt.plot(years, data1, label=country1, color='blue', linewidth=2)
    plt.plot(years, data2, label=country2, color='green', linewidth=2)
    plt.xlabel("Year")
    plt.ylabel(indicator)
    plt.title(f"{indicator} for {country1} and {country2} (2002-2005)")
    plt.legend()
    plt.grid()
    plt.show()

def plot_bar_chart(years, data, country, indicator):
    plt.figure(figsize=(10, 6))
    plt.bar(years, data, color='purple')
    plt.xlabel("Year")
    plt.ylabel(indicator)
    plt.title(f"{indicator} in {country} (2002-2005)")
    plt.show()

def main():
    file_path = 'data.csv'
    indicator = 'Out-of-school children of primary school age, both sexes (number)'
    country1 = 'Ukraine'
    country2 = 'United States'

    years, data_country1, data_country2 = read_data(file_path, indicator, country1, country2)

    if not data_country1:
        print(f"No data found for {country1}. Please check the file.")
    elif not data_country2:
        print(f"No data found for {country2}. Please check the file.")
    else:
        plot_line_chart(years, data_country1, data_country2, country1, country2, indicator)

        selected_country = input("Enter the name of the country for bar chart (Ukraine or United States): ")
        if selected_country == country1:
            plot_bar_chart(years, data_country1, country1, indicator)
        elif selected_country == country2:
            plot_bar_chart(years, data_country2, country2, indicator)
        else:
            print(f"No data available for {selected_country}.")

if __name__ == "__main__":
    main()
