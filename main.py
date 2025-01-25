from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

def generate_resume(font_size, font_color, background_color):
    pdf = canvas.Canvas("Customized_Resume_2.pdf", pagesize=A4)
    
    pdf.setFillColor(HexColor(background_color))
    pdf.rect(0, 0, A4[0], A4[1], fill=True, stroke=False)

    pdf.setFont("Helvetica", font_size)
    pdf.setFillColor(HexColor(font_color))

    image_width = 80
    image_height = 80
    image_x = (A4[0] - image_width) / 2
    image_y = A4[1] - 0.1 * inch - image_height

    pdf.drawImage('Me_1.jpg', x=image_x, y=image_y, width=image_width, height=image_height)

    name = "Venkatakrishnan E"
    contact_info = "vke.1743@gmail.com | +91 9731669548 | Github: Venkat-2341 | Leetcode: venkatt 2341"
    additional_contact = "Codeforces: vke.1743"

    pdf.setFont("Helvetica", font_size + 4)
    pdf.drawCentredString(A4[0]/2, image_y - 30, name)

    pdf.setFont("Helvetica", font_size - 2)
    pdf.drawCentredString(A4[0]/2, image_y - 50, contact_info)
    pdf.drawCentredString(A4[0]/2, image_y - 65, additional_contact)

    text_content = [
        ("Summary", True),
        ("Second-year B.Tech student in Artificial Intelligence at IIT Gandhinagar with expertise in Machine Learning.", False),
        ("Education", True),
        ("B.Tech in Artificial Intelligence, IIT Gandhinagar | 2023–2027", False),
        ("CPI: 8.74 | SPI: 9.18", False),
        ("Grade 10/10 in Machine Learning", False),
        ("Class 12, Geetanjali Olympiad School, Bengaluru | 2023", False),
        ("Grade: 95%", False),
        ("Class 10, National Centre for Excellence, Bengaluru | 2021", False),
        ("Grade: 94.4%", False),
        ("Skills", True),
        ("• Programming Languages: Python, C, C++", False),
        ("• Machine Learning Frameworks: TensorFlow, PyTorch, Keras, Scikit-learn", False),
        ("• Artificial Intelligence: Deep Learning, Generative AI", False),
        ("• Web Development: React.js, FastAPI, JavaScript, CSS", False),
        ("Projects", True),
        ("IDPAC AI (LangChain, Pinecone, Streamlit)", False),
        ("• Intelligent Document Parsing", False),
        ("• Conversational AI Integration", False),
        ("Student Course Management System (FastAPI, SQLAlchemy)", False),
        ("• Designed and developed an end-to-end REST API for managing students and courses using FastAPI.", False),
        ("• Implemented key functionalities such as student registration, course assignment, and grade tracking.", False),
        ("Flight Price Prediction (Flask, Random Forest, Bootstrap)", False),
        ("• Implemented a Flight Price Prediction system using Random Forest, achieving high accuracy.", False),
        ("• Built a user-friendly web interface with Flask and Bootstrap.", False),
        ("Positions of Responsibility", True),
        ("• Class Representative, Artificial Intelligence, IIT Gandhinagar | Aug 2024 -Present", False),
        ("• Senior Marketing Executive, TEDxIITGandhinagar | July 2024 - Present", False),

        ("Achievements", True),
        ("• JEE Advanced 2023: AIR 2341", False),
        ("• JEE Mains 2023: AIR 3464", False)
    ]
    
    x, y = 50, image_y - 100
    line_height = font_size + 6  # Increased line height for more padding
    heading_padding = 15  # Additional padding for headings
    
    for line, is_heading in text_content:
        if is_heading:
            pdf.setFont("Helvetica", font_size + 4)
            y -= heading_padding  # Extra padding before headings
        else:
            pdf.setFont("Helvetica", font_size - 1)
        
        pdf.drawString(x, y, line)
        y -= line_height
    
    pdf.save()
    print("Resume PDF generated successfully as 'Customized_Resume_1.pdf'!!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--font-size", type=int, default=16)
    parser.add_argument("--font-color", type=str, default="#000000")
    parser.add_argument("--background-color", type=str, default="#FFFFFF")
    args = parser.parse_args()

    generate_resume(args.font_size, args.font_color, args.background_color)
    