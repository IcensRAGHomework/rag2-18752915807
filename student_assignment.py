from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(pdf):
    loader = PyPDFLoader(pdf)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    chunks = splitter.split_documents(documents)

    return chunks[-1]

def hw02_2(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    combined_text = "".join([doc.page_content for doc in documents])
    # print(combined_text)
    separators = [
        r"第\s*[一二三四五六七八九十]+\s*章\s",
        r"\n第\s*\d+\s*條",
        r"\n第\s*\d+-\d+\s*條",
        r"第\s*\d+\s*條\n",
        r"第\s*\d+-\d+\s*條\n",
    ]
    splitter = RecursiveCharacterTextSplitter(
        separators=separators,
        chunk_size=10,
        chunk_overlap=0,
        is_separator_regex=True
    )

    chunks = splitter.split_text(combined_text)
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:\n"
              f"{chunk}\n"
              f"{'-' * 40}")
    return len(chunks)

if __name__ == "__main__":
    # last_chunk = hw02_1(q1_pdf)
    # print(last_chunk)
    chunk_count = hw02_2(q2_pdf)
    print(chunk_count)