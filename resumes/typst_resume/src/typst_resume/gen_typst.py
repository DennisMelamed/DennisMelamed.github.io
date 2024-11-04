import json
import ubelt as ub
import typst
from fire import Fire
from typst_funcs import (typst_header, make_section_header,
                         make_personal_header, make_experience_section,
                         make_edu_section, make_skills_section, bib_section)


def gen_typst(input_file_str, output_typ_file_str, output_pdf_file_str):
    input_file_path = ub.Path(input_file_str)
    output_typst_file_path = ub.Path(output_typ_file_str)
    output_pdf_file_path = ub.Path(output_pdf_file_str)

    with input_file_path.open(mode='r') as file:
        json_data = json.load(file)

    typst_source = typst_header
    typst_source += make_personal_header(json_data['name'], [
        json_data['email'], json_data['website'], json_data['location'],
        json_data['github'], json_data['linkedin'], json_data['phone']
    ])
    typst_source += make_section_header("Experience")

    for exp in json_data['experience']:
        typst_source += make_experience_section(exp)

    typst_source += make_section_header("Education")
    for exp in json_data['education']:
        typst_source += make_edu_section(exp)

    typst_source += make_section_header("Skills")
    for key, value in json_data['skills'].items():
        typst_source += make_skills_section(key, value)
    typst_source += make_section_header("Publications")

    typst_source += bib_section(json_data['publications'], "my_pubs.bib",
                                "super_simple_cite.csl")

    with output_typst_file_path.open(mode='w') as file:
        file.write(typst_source)

    typst.compile(str(output_typst_file_path),
                  output=str(output_pdf_file_path))


def process(json_folder: str, pdf_folder: str, typst_folder: str):
    json_folder = ub.Path(json_folder)
    pdf_folder = ub.Path(pdf_folder)
    typst_folder = ub.Path(typst_folder)
    print(json_folder)
    print(typst_folder)
    print(pdf_folder)

    json_folder.ensuredir()
    pdf_folder.ensuredir()
    typst_folder.ensuredir()
    for json_fn in json_folder.glob("*.json"):
        typst_fn = typst_folder / json_fn.augment(ext=".typ").name
        pdf_fn = pdf_folder / json_fn.augment(ext=".pdf").name
        print("generating ", pdf_fn)
        gen_typst(json_fn, typst_fn, pdf_fn)


if __name__ == '__main__':
    #    Fire(gen_typst)
    Fire(process)
    #input_file = ub.Path("2024_10_19.json")
    #output_typst_file = input_file.augment(ext=".typ")
    #output_pdf_file = input_file.augment(ext=".pdf")
    #gen_typst(input_file, output_typst_file, output_pdf_file)
