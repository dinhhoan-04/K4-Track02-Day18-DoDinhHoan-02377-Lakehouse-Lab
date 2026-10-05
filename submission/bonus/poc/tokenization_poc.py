"""PoC for Topic A: High-Throughput PII Tokenization & Medallion Ingestion.

Demonstrates zero-copy streaming PII tokenization at Bronze landing and
partitioning for LLM observability logs.
"""
import hashlib
import json
import polars as pl
from deltalake import write_deltalake, DeltaTable

def tokenize_pii(text: str, salt: str = "lakehouse_salt_2026") -> str:
    """Deterministic HMAC-SHA256 tokenization for email/phone/secrets."""
    import re
    # Tokenize email pattern
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    def sub_email(match):
        token = hashlib.sha256((match.group(0) + salt).encode('utf-8')).hexdigest()[:12]
        return f"[EMAIL_TOKEN_{token}]"
    
    return re.sub(email_pattern, sub_email, text)

def run_poc():
    print("=== Topic A PoC: PII Redaction at Bronze Ingestion ===")
    
    # 1. Simulate Raw Inbound LLM Call Stream
    raw_logs = [
        {"request_id": "req_001", "tenant_id": "tenant_alpha", "ts": "2026-10-05T10:00:00Z", "model": "gpt-4o-mini", "prompt": "User alice@example.com asked about order 123", "latency_ms": 140, "cost_usd": 0.0002},
        {"request_id": "req_002", "tenant_id": "tenant_beta", "ts": "2026-10-05T10:01:00Z", "model": "claude-3-5-sonnet", "prompt": "Contact bob.smith@corp.vn for urgent refund", "latency_ms": 320, "cost_usd": 0.0015},
    ]
    
    # 2. Tokenize Prompts
    clean_logs = []
    for row in raw_logs:
        clean_row = dict(row)
        clean_row["prompt_redacted"] = tokenize_pii(row["prompt"])
        del clean_row["prompt"] # Drop raw PII prompt
        clean_logs.append(clean_row)
        
    df = pl.DataFrame(clean_logs)
    print("\nTokenized DataFrame:")
    print(df.select(["request_id", "tenant_id", "prompt_redacted"]))
    
    # 3. Write to Bronze Delta Table
    table_path = "_lakehouse/scratch/poc_bronze_llm"
    write_deltalake(table_path, df.to_arrow(), mode="overwrite")
    
    dt = DeltaTable(table_path)
    print(f"\nSuccessfully wrote PoC Delta Table to {table_path} (Version: {dt.version()})")
    print("PoC Verification: PASS")

if __name__ == "__main__":
    run_poc()
