import pandas as pd
from refactor.data_processor import process


def test_process():
    df = pd.DataFrame(
        [
            {"first": "John", "last": "Doe", "age": 45, "income": 70000},
            {"first": "Jane", "last": "Smith", "age": 17, "income": None},
            {"first": "Elder", "last": "Lee", "age": 70, "income": 30000},
        ]
    )
    expected_df = pd.DataFrame(
        [
            {
                "full_name": "John Doe",
                "age": 45,
                "income": 70000.0,
                "status": "adult",
            },
            {
                "full_name": "Elder Lee",
                "age": 70,
                "income": 30000.0,
                "status": "senior",
            },
        ]
    )
    output_df = process(df)
    pd.testing.assert_frame_equal(
        output_df.reset_index(drop=True), expected_df
    )
