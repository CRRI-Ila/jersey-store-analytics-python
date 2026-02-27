import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


REQUIRED_COLUMNS = {"Player", "Size", "Quantity", "Price", "Discount"}


def load_data(file_path: str) -> pd.DataFrame:
    """Load CSV data into a DataFrame."""
    return pd.read_csv(file_path)


def validate_columns(df: pd.DataFrame) -> None:
    """Ensure required columns exist."""
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}. "
            f"Found columns: {list(df.columns)}"
        )


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich the dataset."""
    # 1) Duplicates
    num_duplicates = df.duplicated().sum()
    print(f"\nFound {num_duplicates} duplicate rows in the dataset")
    if num_duplicates > 0:
        print("\nSample of duplicate rows:")
        print(df[df.duplicated(keep=False)].head())

    df = df.drop_duplicates().copy()
    print(f"\nRemoved {num_duplicates} duplicates. New shape: {df.shape}")

    # 2) Quantity numeric + fill missing with median
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    median_quantity = df["Quantity"].median()
    df.loc[df["Quantity"].isna(), "Quantity"] = median_quantity

    # 3) Fill missing Size with 'M'
    df.loc[df["Size"].isna(), "Size"] = "M"

    # 4) Recalculate Revenue
    df["Revenue"] = (df["Price"] * df["Quantity"]) - df["Discount"]

    # 5) Feature engineering
    df["HighQuantity"] = df["Quantity"] >= 3
    df["TotalDiscount"] = df["Discount"]

    return df


def most_profitable(df: pd.DataFrame):
    revenue_by_player = df.groupby("Player")["Revenue"].sum()
    return revenue_by_player.idxmax(), revenue_by_player.max()


def least_profitable(df: pd.DataFrame):
    revenue_by_player = df.groupby("Player")["Revenue"].sum()
    return revenue_by_player.idxmin(), revenue_by_player.min()


def plot_and_save(df: pd.DataFrame, out_dir: Path, show: bool = False) -> None:
    """Create plots and save them into images/ folder."""
    out_dir.mkdir(parents=True, exist_ok=True)

    # Figure 1: Total Revenue per Player
    revenue_by_player = df.groupby("Player")["Revenue"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 4))
    plt.bar(revenue_by_player.index.astype(str), revenue_by_player.values)
    plt.title("Total Revenue per Player")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / "revenue_per_player.png", dpi=200)
    if show:
        plt.show()
    plt.close()

    # Figure 2: Quantity Distribution (Pie)
    quantity_counts = df["Quantity"].value_counts().sort_index()
    plt.figure(figsize=(5, 5))
    plt.pie(quantity_counts, labels=quantity_counts.index.astype(str), autopct="%1.1f%%")
    plt.title("Quantity Distribution")
    plt.tight_layout()
    plt.savefig(out_dir / "quantity_distribution.png", dpi=200)
    if show:
        plt.show()
    plt.close()

    # Figure 3: Jersey Size Distribution
    size_counts = df["Size"].value_counts()
    plt.figure(figsize=(6, 4))
    plt.bar(size_counts.index.astype(str), size_counts.values)
    plt.title("Jersey Size Distribution")
    plt.xlabel("Size")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_dir / "size_distribution.png", dpi=200)
    if show:
        plt.show()
    plt.close()

    # Figure 4: Scatter - Total Quantity vs Price per Player
    grouped = df.groupby("Player")
    player_names, total_quantities, player_prices = [], [], []
    for name, group in grouped:
        player_names.append(name)
        total_quantities.append(group["Quantity"].sum())
        player_prices.append(group["Price"].iloc[0])

    plt.figure(figsize=(7, 5))
    plt.scatter(total_quantities, player_prices, s=80)
    for i in range(len(player_names)):
        plt.text(total_quantities[i] + 0.2, player_prices[i], str(player_names[i]), fontsize=9)
    plt.title("Total Quantity Sold vs Price per Player")
    plt.xlabel("Total Quantity Sold")
    plt.ylabel("Price ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_dir / "quantity_vs_price_scatter.png", dpi=200)
    if show:
        plt.show()
    plt.close()

    # Figure 5: High Quantity Orders per Player
    high_quantity_counts = df[df["HighQuantity"]].groupby("Player").size().sort_values(ascending=False)
    plt.figure(figsize=(8, 4))
    plt.bar(high_quantity_counts.index.astype(str), high_quantity_counts.values)
    plt.title("High Quantity Orders per Player (Quantity ≥ 3)")
    plt.xlabel("Player")
    plt.ylabel("High Quantity Orders")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / "high_quantity_orders.png", dpi=200)
    if show:
        plt.show()
    plt.close()

    # Figure 6: Total Discount per Player
    total_discount_by_player = df.groupby("Player")["TotalDiscount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 4))
    plt.bar(total_discount_by_player.index.astype(str), total_discount_by_player.values)
    plt.title("Total Discount Given per Player")
    plt.xlabel("Player")
    plt.ylabel("Total Discount ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out_dir / "total_discount_per_player.png", dpi=200)
    if show:
        plt.show()
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Jersey store sales profitability analysis")
    parser.add_argument(
        "--data",
        type=str,
        default="data/jersey_sales_sample.csv",
        help="Path to CSV dataset (default: data/jersey_sales_sample.csv)",
    )
    parser.add_argument(
        "--save-plots",
        action="store_true",
        help="Save plots into images/ (recommended for GitHub README)",
    )
    parser.add_argument(
        "--show-plots",
        action="store_true",
        help="Display plots on screen (optional)",
    )
    args = parser.parse_args()

    # Load + validate
    df_raw = load_data(args.data)
    validate_columns(df_raw)

    # Clean + analyze
    df = clean_data(df_raw)

    # Data quality check
    print("\n=== Data Quality Check ===")
    print("\nMissing values after cleaning:")
    print(df.isna().sum())
    print("\nData types:")
    print(df.dtypes)

    # Results
    player_max, revenue_max = most_profitable(df)
    player_min, revenue_min = least_profitable(df)

    print("\nMost Profitable Player:")
    print("Player:", player_max)
    print("Total Revenue: $", round(float(revenue_max), 2))

    print("\nLeast Profitable Player:")
    print("Player:", player_min)
    print("Total Revenue: $", round(float(revenue_min), 2))

    # Plots
    if args.save_plots or args.show_plots:
        plot_and_save(df, out_dir=Path("images"), show=args.show_plots)
        if args.save_plots:
            print("\nSaved plots into: images/")


if __name__ == "__main__":
    main()
