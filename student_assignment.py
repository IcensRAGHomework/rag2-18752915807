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

    separators = [
        r" 第\s*[一二三四五六七八九十百千]+\s*章 ",
        r"第\s*\d+\s*條 ",
        # r"第\s*\d+-\d+\s*條",
        r"\n第\s*\d+-\d+\s*條",
    ]
    splitter = RecursiveCharacterTextSplitter(
        separators=separators,
        chunk_size=80,
        chunk_overlap=0,
        is_separator_regex=True
    )

    chunks = splitter.split_documents(documents)
    #
    # page_chunk_counts = {}
    # for chunk in chunks:
    #     page_number = chunk.metadata.get('page', 'Unknown')
    #     if page_number in page_chunk_counts:
    #         page_chunk_counts[page_number] += 1
    #     else:
    #         page_chunk_counts[page_number] = 1
    #
    # chunk_counts_list = [page_chunk_counts.get(page, 0) for page in range(len(documents))]
    #
    for i, chunk in enumerate(chunks):
        page_number = chunk.metadata.get('page', 'Unknown')
        print(f"Chunk {i + 1} (Page {page_number + 1}):\n"
              f"{chunk.page_content}\n"
              f"{'-' * 40}")
    #
    # for page, count in enumerate(chunk_counts_list):
    #     print(f"Page {page + 1} has {count} chunks")

    return len(chunks)

if __name__ == "__main__":
    # last_chunk = hw02_1(q1_pdf)
    # print(last_chunk)
    chunk_count = hw02_2(q2_pdf)
    print(chunk_count)