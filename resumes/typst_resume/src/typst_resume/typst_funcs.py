import ubelt as ub

typst_header = ub.codeblock('''
#show heading: set text(font: "Linux Biolinum")

#show link: underline

// Uncomment the following lines to adjust the size of text
// The recommend resume text size is from `10pt` to `12pt`
#set text(
  size: 10pt,
)

// Feel free to change the margin below to best fit your own CV
#set page(
  margin: (x: 0.9cm, y: 0.9cm),
)

// For more customizable options, please refer to official reference: https://typst.app/docs/reference/

#set par(justify: true)

#show link: underline
#show link: set text(blue)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}
\n
''')


def make_section_header(section_name):
    return f"== {section_name}\n#chiline()\n"


def make_linkable(elem):
    if ".com" in elem or ".me" in elem:
        return f"#link(\"{elem}\")"
    return elem


def make_personal_header(name, elements):
    header = ""
    header += "\n#set align(center) \n"

    header += f"\n\n= {name}\n"

    for eidx in range(0, len(elements), 3):
        header += make_linkable(elements[eidx]) + " | " + make_linkable(
            elements[eidx + 1]) + " | " + make_linkable(
                elements[eidx + 2]) + "\\\n"

    header += "\n#set align(left) \n"
    return header


def make_experience_section(experience):
    role = experience['position']
    comp = experience['company']
    sd = experience['start_date']
    ed = experience['end_date']
    exp_header = f"*{comp}*, _{role}_  #h(1fr) {sd} -- {ed} \\"
    exp_header += '\n'
    notes = []
    for note in experience['notes']:
        notes.append(f"- {note}")
    exp = exp_header + "\n".join(notes) + "\n\n"
    return exp


def make_edu_section(edu):
    sd = edu['start_date']
    ed = edu['end_date']
    edu_block = f"*{edu['degree']}* #h(1fr) {sd} -- {ed} \\\n"
    advisor = ""
    if 'advisor' in edu:
        advisor = edu['advisor']
    edu_block += f"{edu['university']}, {advisor} #h(1fr) {edu['location']} \\\n"
    if 'thesis' in edu:
        edu_block += f"- Thesis: {edu['thesis']} \\\n"
    if "selected_coursework" in edu:
        edu_block += "- Selected Coursework: "
        edu_block += ", ".join(edu['selected_coursework'])
        edu_block += "\\\n"
    if 'notes' in edu:
        for note in edu['notes']:
            edu_block += f"- {note}\n"
    return edu_block


def make_skills_section(name, skills):
    skills_str = ", ".join(skills)
    block = f"*{name}*: {skills_str}\\\n"
    return block


def bib_section(cites_to_include, bib_file, cite_style_file):
    bib = ""
    for c in cites_to_include:
        bib += f"#cite(<{c}>, form:none)\n"
    bib += f"#bibliography(\"{bib_file}\", title:none, style:\"{cite_style_file}\")"
    return bib
