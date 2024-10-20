import ubelt as ub


typst_header = ub.codeblock(
'''
#show heading: set text(font: "Linux Biolinum")

#show link: underline

// Uncomment the following lines to adjust the size of text
// The recommend resume text size is from `10pt` to `12pt`
// #set text(
//   size: 12pt,
// )

// Feel free to change the margin below to best fit your own CV
#set page(
  margin: (x: 0.9cm, y: 1.3cm),
)

// For more customizable options, please refer to official reference: https://typst.app/docs/reference/

#set par(justify: true)

#let chiline() = {v(-3pt); line(length: 100%); v(-5pt)}
\n
'''
)

def make_section_header(section_name):
    return f"== {section_name}\n#chiline()\n"

def make_personal_header(name, elements):
    header = ""
    header += "\n#set align(center) \n"
    header += f"\n\n= {name}\n"
    for eidx in range(0, len(elements), 3):
        header += elements[eidx] + " | " + elements[eidx + 1] + " | " + elements[eidx+2] + "\n\n"
    header += "\n#set align(left) \n"
    return header

