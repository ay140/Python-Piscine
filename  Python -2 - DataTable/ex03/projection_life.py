from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads GDP and Life Expectancy datasets, filters the data for
    the year 1900 across all countries, and plots it as a scatter plot.
    """
    try:
        # Load the datasets
        gdp_df = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_df = load("life_expectancy_years.csv")

        if gdp_df is None or life_df is None:
            return

        year = "1900"

        if year not in gdp_df.columns or year not in life_df.columns:
            print(f"Year {year} not found in the datasets.")
            return

        # In order to safely plot them side by side, we should make
        # sure we are pairing values of the same countries.
        # We'll merge them by country to ensure precise mapping.
        gdp_sub = gdp_df[['country', year]].rename(columns={year: 'gdp'})
        life_sub = life_df[['country', year]].rename(columns={year: 'life'})

        merged_df = gdp_sub.merge(life_sub, on='country').dropna()

        # Some lines might have string representations like '1.2k' for gdp
        def parse_gdp(val):
            if isinstance(val, str):
                if val.endswith('k'):
                    return float(val[:-1]) * 1000
                elif val.endswith('M'):
                    return float(val[:-1]) * 1000000
            return float(val)

        x_gdp = merged_df['gdp'].apply(parse_gdp)
        y_life = merged_df['life']

        # Plot
        plt.figure(figsize=(10, 6))

        # We scatter GDP vs Life Expectancy
        plt.scatter(x_gdp, y_life, color='blue', alpha=0.6)

        plt.title(f"{year} Life expectancy / Gross domestic product")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")

        # Usually, x-axis for GDP is better in log scale to see correlation
        # The image might require it, but we set simple ticks or scale
        # Subject specifies 1k, 10k style typically. We'll use continuous
        # xscale log to make sense of the GDP grouping.
        plt.xscale("log")

        # format xticks
        # standard gapminder curves: 300, 1000, 10000
        ticks = [300, 1000, 10000]
        labels = ['300', '1k', '10k']
        plt.xticks(ticks, labels)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
