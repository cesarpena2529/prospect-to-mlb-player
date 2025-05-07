import pandas as pd

# Load datasets
aa_std = pd.read_csv("AA2006-2024Standard.csv")
aa_adv = pd.read_csv("AA2006-2024Advanced.csv")
aaa_std = pd.read_csv("AAA2006-2024Standard.csv")
aaa_adv = pd.read_csv("AAA2006-2024Advanced.csv")

# Merge standard and advanced datasets for AA
aa_merged = pd.merge(
    aa_std.add_suffix("_std"), 
    aa_adv.add_suffix("_adv"), 
    left_on=["Name_std", "Team_std", "Season_std"], 
    right_on=["Name_adv", "Team_adv", "Season_adv"],
    how="inner"
)
aa_merged["level"] = "AA"

# Merge standard and advanced datasets for AAA
aaa_merged = pd.merge(
    aaa_std.add_suffix("_std"), 
    aaa_adv.add_suffix("_adv"), 
    left_on=["Name_std", "Team_std", "Season_std"], 
    right_on=["Name_adv", "Team_adv", "Season_adv"],
    how="inner"
)
aaa_merged["level"] = "AAA"

# Combine AA and AAA
combined_df = pd.concat([aa_merged, aaa_merged], ignore_index=True)

# Save final combined file
combined_df.to_csv("minor_league_combined.csv", index=False)
print("✅ minor_league_combined.csv created successfully.")
