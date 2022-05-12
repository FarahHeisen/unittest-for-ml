import pandas as pd
import typer
from dataframe.dataframe import process

app = typer.Typer()


@app.command()
def process_csv(csv: str):
    file_name = csv.split("/")[-1]
    input_dataframe = pd.read_csv(csv, sep=";")
    output_dataframe = process(df=input_dataframe)
    output_dataframe.to_csv(f"output_{file_name}")
    typer.echo("processed")


if __name__ == "__main__":
    app()
