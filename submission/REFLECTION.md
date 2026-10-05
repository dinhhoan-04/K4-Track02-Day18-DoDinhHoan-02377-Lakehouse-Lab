# Lakehouse Reflection & Anti-Pattern Analysis

**Anti-Pattern:** *Stale External Vector Index Desynchronization (Tái hiện tại NB7)*

**Phân tích & Phòng tránh:**
Trong các hệ thống RAG/Multimodal Production, việc tách rời bảng Lakehouse (Delta/Iceberg) chứa dữ liệu nguồn và Vector Index bên ngoài (Milvus/Pinecone) rất dễ vướng anti-pattern mất đồng bộ sự kiện xóa. Khi câu lệnh DELETE/GDPR được thực thi trên Lakehouse, transaction log ghi nhận tombstone nhưng external index không tự động nhận Change Data Capture (CDC). Hậu quả là Vector Search vẫn trả về kết quả đã bị xóa (0 hits trong Lakehouse nhưng >0 hits ở Vector DB). Để phòng tránh, hệ thống cần áp dụng Native Vector Tables (như Lance/Delta Vector) hoặc thiết lập pipeline CDC từ Delta Change Feed trực tiếp đẩy Tombstone Event giải phóng vector index synchronous trước khi commit transaction.

**Khai báo sử dụng AI:**
AI (Gemini 3.6 Flash) được sử dụng để giải thích cơ chế transaction log, hỗ trợ kiểm thử script tự động và rà soát các tiêu chí rubric. Toàn bộ notebook, kết quả đo đạc và nội dung phân tích đều được tự thực thi và xác minh độc lập.
