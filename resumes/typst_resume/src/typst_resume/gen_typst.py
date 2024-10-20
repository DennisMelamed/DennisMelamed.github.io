import json
import ubelt as ub
from typst_funcs import typst_header, make_section_header, make_personal_header
import typst




input_file_str = "2024_10_19.json"
input_file_path = ub.Path(input_file_str)
output_typst_file_path = input_file_path.augment(ext=".typ")
output_pdf_file_path = input_file_path.augment(ext=".pdf")

with input_file_path.open(mode='r') as f:
    json_data = json.load(f)


typst_source = typst_header
typst_source += make_personal_header(json_data['name'],
                                     [json_data['email'].replace("@", "\@"),
                                      json_data['website'],
                                      json_data['location'],
                                      json_data['github'],
                                      json_data['linkedin'],
                                      json_data['phone']])
typst_source += make_section_header("Experience")
typst_source += make_section_header("Education")
typst_source += make_section_header("Skills")
typst_source += make_section_header("Publications")

typst_source += "#bibliography(\"my_pubs.bib\", title:none, full:true, style:\"super_simple_cite.csl\")"


with output_typst_file_path.open(mode='w') as f:
    f.write(typst_source)

typst.compile(str(output_typst_file_path), output=str(output_pdf_file_path))
