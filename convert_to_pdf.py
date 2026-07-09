import subprocess
import os

def convert_to_pdf(docx_path):
    try:
        subprocess.run(
            [
                "libreoffice",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                os.path.dirname(docx_path),
                docx_path,
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        return os.path.splitext(docx_path)[0] + ".pdf"

    except subprocess.CalledProcessError as e:
        print("PDF conversion failed.")
        print(e.stderr)
        return None
