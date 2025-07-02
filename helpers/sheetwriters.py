import pandas as pd
import re


_INVALID_TITLE_REGEX = re.compile('[\\\\*?:/\\[\\]]')

def spread(df: pd.DataFrame, filename: str, sheet_names: list[str]=None,
            key: str=None, engine: str="openpyxl"):

    if filename.endswith('.xlsx'):
        if engine not in ["openpyxl", "xlsxwriter"]:
            msg = f"Invalid engine: {engine} for xlsx-file."
            raise ValueError(msg)

    elif filename.endswith('.ods'):
        engine="odswriter"

    else:
        msg = f"Invalid or missing filetype: .{filename.split('.')[-1]}"
        raise ValueError(msg)

    if key:
        cols = [col for col in df.columns if col != key]
        if not sheet_names:
            sheet_names = df[key].drop_duplicates()

        with pd.ExcelWriter(filename, engine=engine) as writer:
            sheet_names.to_excel(writer, sheet_name="Index", index=False, header=False)
            if engine == "xlsxwriter":
                    writer.sheets["Index"].autofit()

            for sheet in sheet_names:
                sheet_name = _INVALID_TITLE_REGEX.sub(' ', sheet)[:31]
                df[df[key] == sheet_name][cols].to_excel(writer, 
                    sheet_name=sheet_name, index=False)
                if engine == "xlsxwriter":
                    writer.sheets[sheet_name].autofit()

    else:
        if sheet_names:
            if len(sheet_names) > 1:
                raise ValueError(f"Need key")
            else:
                sheet_name = sheet_names[0]
        
        else:
            sheet_name = "Sheet 1"

        with pd.ExcelWriter(filename, engine=engine) as writer:
            df.to_excel(writer, index=False)
            if engine == "xlsxwriter":
                writer.sheets[sheet_name].autofit()


if __name__ == "__main__":
    df = pd.DataFrame({ "foo": ["a", "b", "c"], 
                        "bar": [1, 2, 3], 
                        "sheet": ["Sheet1", "Sheet1", "Sheet2"]})
                        
    spread(df, "foobar.xlsx", key="sheet", engine="xlsxwriter")
