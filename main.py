from pathlib import Path
import cv2
from matplotlib import pyplot as plt
from IPython.core.display import HTML

import deepdoctection as dd
#  data from here https://github.com/deepdoctection/notebooks/blob/main/Get_Started.ipynb

doc_path = Path.cwd() / "data/pdf/9780357517239.pdf"

analyzer = dd.get_dd_analyzer(config_overwrite=["DEVICE='cpu'"])

df = analyzer.analyze(path=doc_path)
df.reset_state()


doc = iter(df)

for page in doc:
    type(page)

    print(
        f" height: {page.height} \n width: {page.width} \n file_name: {page.file_name} \n document_id: {page.document_id} \n image_id: {page.image_id}\n"
    )

    pg_attributes = page.get_attribute_names()


    print(f"Attributes: {pg_attributes} \n")

    print(f"Text: {page.text} \n")

    for layout in page.layouts:
        if layout.category_name == "title":
            print(f"Title: {layout.text} \n")
        print(
            f"Layout: {layout.category_name} (ORDER: {layout.reading_order}), {layout.text}"
        )

    print(f"Tables {len(page.tables)}")

    if len(page.tables) > 0:
        table = page.tables[0]
        print(f"First Table text: {table.text}")
    print("\n")
