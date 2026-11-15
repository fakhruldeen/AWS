# Master Architecture Blueprint: Amazon S3 Storage Lifecycle & Tiers

> **Category:** Cloud Storage & Cost Optimization  
> **Course:** AWS Certified Cloud Practitioner (CLF-C02)  
> **Tags:** `#diagram` `#s3` `#storage` `#lifecycle`

```mermaid
flowchart TD
    Ingest["New Object Uploaded via S3 API"] --> Standard["1. S3 Standard<br/>(Active frequent access, $0.023/GB/mo, 3+ AZs)"]

    Standard -->|"Unknown or dynamic access patterns"| IntelTier["2. S3 Intelligent-Tiering<br/>(Auto-moves between tiers with $0 retrieval fees)"]

    Standard -->|"After 30 Days (Predictable Infrequent)"| StdIA["3. S3 Standard-IA<br/>(Infrequent access, rapid retrieval, 3+ AZs)"]
    
    Standard -.->|"Non-critical reproducible data"| OneZoneIA["4. S3 One Zone-IA<br/>(Single AZ only, saves 20% cost)"]

    StdIA -->|"After 90 Days (Long-term Archive)"| GlacierFlex["5. S3 Glacier Flexible Retrieval<br/>(Cold storage, retrieve in min to hours)"]

    GlacierFlex -->|"After 180 Days (Permanent Compliance Archive)"| DeepArchive["6. S3 Glacier Deep Archive<br/>(Lowest cost: $0.00099/GB/mo, 12-48h)"]

    DeepArchive -->|"After 7 Years / 2555 Days"| Expire["7. Object Expiration / Permanent Deletion"]
```

### Exam Decision Matrix:
- **Immediate access, active website images:** `S3 Standard`
- **Unknown or fluctuating patterns:** `S3 Intelligent-Tiering`
- **Disaster recovery secondary backups:** `S3 Standard-IA`
- **Replaceable thumbnails / non-critical:** `S3 One Zone-IA`
- **Archived financial records (1-3 times/year):** `S3 Glacier Flexible Retrieval`
- **Legal hold / compliance data kept for 10 years, rarely accessed:** `S3 Glacier Deep Archive`
