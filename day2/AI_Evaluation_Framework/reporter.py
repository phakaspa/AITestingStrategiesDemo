import pandas as pd


def save_report(results):
    df = pd.DataFrame(results)

    df.to_csv(
        "evaluation_results.csv",
        index=False,
    )

    df.to_excel(
        "evaluation_results.xlsx",
        index=False,
    )

    print("\nEvaluation report saved.")
    print("Files: evaluation_results.csv")
    print("       evaluation_results.xlsx")

    return df
