
import streamlit as st
import os
import uuid
import pandas as pd

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Load metadata
metadata_file = "metadata.csv"
if os.path.exists(metadata_file):
    df = pd.read_csv(metadata_file)
else:
    df = pd.DataFrame(columns=["id", "filename", "description", "path"])

st.title("📁 KHO DỮ LIỆU THỬ NGHIỆM")

# Upload Section
st.header("📤 Tải dữ liệu lên")
uploaded_file = st.file_uploader("Chọn file bất kỳ", type=None)
desc = st.text_input("Mô tả tài liệu")

if st.button("Tải lên") and uploaded_file:
    file_id = str(uuid.uuid4())
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}_{uploaded_file.name}")
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())
    df = pd.concat([df, pd.DataFrame([{
        "id": file_id,
        "filename": uploaded_file.name,
        "description": desc,
        "path": save_path
    }])], ignore_index=True)
    df.to_csv(metadata_file, index=False)
    st.success("✅ Tải file thành công!")

# Display Section
st.header("📚 Danh sách tài liệu")
if len(df) > 0:
    for i, row in df.iterrows():
        with st.expander(f"📄 {row['filename']}"):
            st.write("📝 Mô tả:", row["description"])
            if row["filename"].lower().endswith((".png", ".jpg", ".jpeg")):
                st.image(row["path"])
            elif row["filename"].lower().endswith(".pdf"):
                st.write(f"[📄 Xem PDF]({row['path']})")
            elif row["filename"].lower().endswith((".xlsx", ".xls")):
                try:
                    df_xl = pd.read_excel(row["path"])
                    st.dataframe(df_xl)
                except Exception as e:
                    st.error("Không đọc được file Excel")
            else:
                st.write("📁 Đường dẫn:", row["path"])

            new_desc = st.text_input("✏️ Sửa mô tả", value=row["description"], key=row["id"])
            if st.button("Cập nhật mô tả", key="update_" + row["id"]):
                df.loc[i, "description"] = new_desc
                df.to_csv(metadata_file, index=False)
                st.success("Đã cập nhật mô tả")

            if st.button("🗑️ Xóa", key="delete_" + row["id"]):
                if os.path.exists(row["path"]):
                    os.remove(row["path"])
                df.drop(i, inplace=True)
                df.to_csv(metadata_file, index=False)
                st.success("Đã xóa file")
                st.experimental_rerun()
else:
    st.info("Chưa có dữ liệu nào được tải lên.")
