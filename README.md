Customizable Resume PDF Generator

Objective

This Python command-line script allows users to generate a customized resume in PDF format with options for adjusting font size, font color, and background color.

Features

Pre-generated Resume

The resume contains essential sections such as:

Name

Contact Information

Skills

Education

Experience

The initial PDF is generated using the ReportLab library.

Resume PDF Layout

The resume layout is inspired by modern resume templates from websites such as:

Canva

Enhancv

Resume Genius

Resume Builder

Resume.io

Customization Options

The script allows customization through command-line arguments:

--font-size: Adjust the font size.

--font-color: Adjust the font color using a hex code (e.g., #000000).

--background-color: Adjust the background color using a hex code (e.g., #FFFFFF).

PDF Regeneration

The PDF is regenerated with the chosen options and saved as a new file.

Tools/Frameworks Used

argparse: For parsing command-line arguments.

ReportLab: For generating customized PDF files.

Setup Instructions

Prerequisites

Ensure you have Python installed on your system. The script requires the following dependencies:

pip install reportlab

Usage

Run the script with desired customization options:

python resume_generator.py --font-size 14 --font-color "#FF5733" --background-color "#FFFFFF"

Example

Generating a resume with default settings:

python resume_generator.py

Customizing font size, color, and background color:

python resume_generator.py --font-size 12 --font-color "#0000FF" --background-color "#F5F5F5"

Deliverables

A Python script (resume_generator.py) that accepts customization arguments and outputs a customized PDF file.

A sample resume PDF created using the script.

The script and sample resume PDF uploaded to a public GitHub repository.

The repository URL should be shared with the company.

Example Scenarios

User wants to generate a resume with a larger font size:

python resume_generator.py --font-size 18

User wants a colorful resume:

python resume_generator.py --font-color "#FF0000" --background-color "#000000"

Contact

For any issues or queries, please reach out at: vke.1743@gmail.com