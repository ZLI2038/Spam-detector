
import pandas as pd
from docx import Document
from detector import detect_spam, detect_spam_batch

def process_file(file_path, model):
    try:
        if file_path.endswith(".txt"):
            with open(file_path, 'r', encoding="utf-8") as f:
                text = f.read()
            result = detect_spam(text, model)
            return f"[TXT] 检测结果：{result}\n\n{text[:300]}..."

        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path, encoding="utf-8")
            if "text" not in df.columns:
                return "CSV 文件中未找到 'text' 列。"
            labels = detect_spam_batch(df["text"], model)
            df["result"] = labels
            return f"[CSV] 共检测 {len(df)} 条记录：\n" + df[["text", "result"]].head().to_string(index=False)

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            full_text = "\n".join([para.text for para in doc.paragraphs])
            result = detect_spam(full_text, model)
            return f"[DOCX] 检测结果：{result}\n\n{full_text[:300]}..."

        else:
            return "不支持的文件类型。支持：.txt, .csv, .docx"

    except Exception as e:
        return f"读取文件出错：{e}"
