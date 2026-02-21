from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads life expectancy data, extracts the data for the campus country
    (United Arab Emirates), and plots it as a line graph.
    """
    try:
        # Load the dataset
        df = load("life_expectancy_years.csv")
        if df is None:
            return

        # Find the campus country
        country = "United Arab Emirates"
        country_data = df[df['country'] == country]

        if country_data.empty:
            print(f"Country '{country}' not found in the dataset.")
            return

        # Extract years and life expectancy values
        # The first column is 'country', the rest are years
        years = country_data.columns[1:].astype(int)
        life_expectancy = country_data.iloc[0, 1:]

        # Create the plot
        plt.figure(figsize=(10, 6))
        plt.plot(years, life_expectancy)

        # Set the title and labels
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")

        # Select a reasonable number of x-ticks to display
        plt.xticks(range(1800, 2100, 40))

        # Adjust layout
        plt.tight_layout()

        # Display the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
