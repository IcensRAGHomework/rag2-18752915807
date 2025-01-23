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

    return chunks

def hw02_2(pdf):
    # 使用 PyPDFLoader 加载 PDF 文件
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()

    separators = ["\n第[0-9]+條", "\n第[一二三四五六七八九十]+章", "\n", "。", "；"]

    splitter = RecursiveCharacterTextSplitter(separators=separators, chunk_size=2000, chunk_overlap=0, keep_separator=True)

    # 分割文本内容
    chunks = splitter.split_documents(documents)
    print(chunks)
    # 返回得到的 chunks 数量
    return len(chunks)

if __name__ == "__main__":
    last_chunk = hw02_1(q1_pdf)
    print(last_chunk)
    chunk_count = hw02_2(q2_pdf)
    print(chunk_count)