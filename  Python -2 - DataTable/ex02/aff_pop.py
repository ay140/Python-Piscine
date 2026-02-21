from load_csv import load
import matplotlib.pyplot as plt


def process_population(pop_str):
    """
    Parses a population string containing an 'M' or 'k' suffix and
    returns the float value in millions. For example, '65M' -> 65.0,
    '31.2M' -> 31.2, '500k' -> 0.5.
    """
    if isinstance(pop_str, str):
        if pop_str.endswith('M'):
            return float(pop_str[:-1])
        elif pop_str.endswith('k'):
            return float(pop_str[:-1]) / 1000
        elif pop_str.endswith('B'):
            return float(pop_str[:-1]) * 1000
    return float(pop_str)


def main():
    """
    Loads population data, compares United Arab Emirates and France,
    and plots them as a line graph from 1800 to 2050.
    """
    try:
        # Load the dataset
        df = load("population_total.csv")
        if df is None:
            return

        # Define countries
        campus_country = "United Arab Emirates"
        other_country = "France"

        campus_data = df[df['country'] == campus_country]
        other_data = df[df['country'] == other_country]

        if campus_data.empty or other_data.empty:
            print("One of the countries was not found in the dataset.")
            return

        # Prepare the range of years (1800 to 2050)
        # We need to filter the columns to just this range
        columns = df.columns[1:]  # Exclude 'country'
        years_to_plot = [str(year) for year in range(1800, 2051)]
        valid_years = [y for y in years_to_plot if y in columns]

        if not valid_years:
            print("No valid years found in the dataset in range 1800-2050.")
            return

        # Extract population data for the valid years
        campus_pop = campus_data[valid_years].iloc[0].apply(process_population)
        other_pop = other_data[valid_years].iloc[0].apply(process_population)

        # Convert valid years back to int for x-axis
        x_years = [int(y) for y in valid_years]

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(x_years, campus_pop, label=campus_country, color="blue")
        plt.plot(x_years, other_pop, label=other_country, color="green")

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc="lower right")

        # Set specific ticks for x-axis (every 40 years as per ex01 convention)
        plt.xticks(range(1800, 2051, 40))

        # Y axis formatting (e.g. 20M, 40M, 60M)
        max_pop = max(campus_pop.max(), other_pop.max())
        plt.yticks(
            range(0, int(max_pop) + 20, 20),
            [f"{i}M" for i in range(0, int(max_pop) + 20, 20)]
        )

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
