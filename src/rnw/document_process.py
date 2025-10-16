from pypdf import PdfReader


def extract(path: str):
    reader = PdfReader(path)
    page = reader.get_page(0)
    print(page.extract_text())


class DocumentProcess:
    pass